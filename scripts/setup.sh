#!/usr/bin/env bash
# One-time setup: creates your GitHub repo, pushes this folder, and creates milestones and issues.
# Usage: ./scripts/setup.sh [--public | --private] [YYYY-MM-DD]
#   --public (default) makes the repo visible to anyone; --private keeps it to you.
#   The date is the Monday you start week 1 (default: 2026-10-12).
set -euo pipefail
cd "$(dirname "$0")/.."

VIS="--public"; START="2026-10-12"
for a in "$@"; do
  case "$a" in
    --public) VIS="--public" ;;
    --private) VIS="--private" ;;
    20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) START="$a" ;;
    *) echo "Unknown option: $a"; exit 1 ;;
  esac
done

if ! command -v git >/dev/null 2>&1; then
  echo "Git is missing. Run: xcode-select --install   then re-run this script."; exit 1
fi
if ! command -v gh >/dev/null 2>&1; then
  if command -v brew >/dev/null 2>&1; then
    echo "Installing the GitHub CLI with Homebrew…"; brew install gh
  else
    echo "Install the GitHub CLI from https://cli.github.com (or install Homebrew first), then re-run."; exit 1
  fi
fi
if ! gh auth status >/dev/null 2>&1; then
  echo "Signing in to GitHub (a browser window will open)…"
  gh auth login --web --git-protocol https
fi
gh auth setup-git >/dev/null 2>&1 || true

LOGIN="$(gh api user -q .login)"
if ! git config --global user.name >/dev/null; then git config --global user.name "$LOGIN"; fi
if ! git config --global user.email >/dev/null; then
  git config --global user.email "$(gh api user -q .id)+${LOGIN}@users.noreply.github.com"
fi

NAME="$(basename "$PWD")"
[ -d .git ] || git init -q -b main
git config pull.rebase true
git config core.hooksPath scripts/hooks
git add -A
git commit -q -m "Start ML journey" || true

if ! git remote get-url origin >/dev/null 2>&1; then
  if gh repo view "$LOGIN/$NAME" >/dev/null 2>&1; then
    git remote add origin "https://github.com/$LOGIN/$NAME.git"
    git push -u origin main
  else
    gh repo create "$NAME" "$VIS" --source=. --remote=origin --push
  fi
else
  git push -u origin main
fi

python3 scripts/create_issues.py ${START:+--start "$START"}

# Private companion repo in ./private (ignored by the public repo)
(
  cd private
  [ -d .git ] || git init -q -b main
  git config pull.rebase true
  mkdir -p .git/hooks && cp ../scripts/hooks/pre-commit .git/hooks/pre-commit
  git add -A
  git commit -q -m "Start private companion repo" || true
  if ! git remote get-url origin >/dev/null 2>&1; then
    if gh repo view "$LOGIN/$NAME-private" >/dev/null 2>&1; then
      git remote add origin "https://github.com/$LOGIN/$NAME-private.git"; git push -u origin main
    else
      gh repo create "$NAME-private" --private --source=. --remote=origin --push
    fi
  fi
)
gh workflow run progress.yml >/dev/null 2>&1 || true

echo
echo "All set: https://github.com/$LOGIN/$NAME  (private companion: https://github.com/$LOGIN/$NAME-private)"
echo "Paste  $LOGIN/$NAME  into the “Your GitHub repo” box on the syllabus page."
