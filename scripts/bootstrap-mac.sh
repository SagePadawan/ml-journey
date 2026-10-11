#!/usr/bin/env bash
# One-command setup for the ML Journey on an Apple Silicon Mac.
#
# Paste into Terminal (keep the bash -c form so sign-in prompts work):
#   bash -c "$(curl -fsSL https://raw.githubusercontent.com/SagePadawan/ml-journey/main/scripts/bootstrap-mac.sh)"
# Or, from inside a clone:  ./scripts/bootstrap-mac.sh
#
# Safe to re-run: it skips anything already installed.
set -euo pipefail

say()  { printf "\n\033[1m==> %s\033[0m\n" "$1"; }
fail() { printf "\n\033[31mStopped: %s\033[0m\n" "$1"; exit 1; }

[ "$(uname -s)" = "Darwin" ] || fail "this script is for macOS."
[ "$(uname -m)" = "arm64" ]  || fail "this script is for Apple Silicon Macs."

# ---------- Homebrew ----------
if ! command -v brew >/dev/null 2>&1 && [ ! -x /opt/homebrew/bin/brew ]; then
  say "Installing Homebrew (asks for your Mac password once)"
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi
eval "$(/opt/homebrew/bin/brew shellenv)"
grep -q 'brew shellenv' "$HOME/.zprofile" 2>/dev/null || echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> "$HOME/.zprofile"

say "Installing command-line tools: git, GitHub CLI, uv, OpenMP"
for f in git gh uv libomp; do
  brew list --formula "$f" >/dev/null 2>&1 || brew install "$f"
done

say "Installing apps: VS Code and GitHub Desktop (skipped if already installed)"
[ -d "/Applications/Visual Studio Code.app" ] || brew install --cask visual-studio-code
[ -d "/Applications/GitHub Desktop.app" ]     || brew install --cask github

# ---------- GitHub ----------
if ! gh auth status >/dev/null 2>&1; then
  say "Signing in to GitHub (a browser window opens)"
  gh auth login --web --git-protocol https
fi
gh auth setup-git >/dev/null 2>&1 || true
LOGIN="$(gh api user -q .login)"
git config --global user.name  >/dev/null || git config --global user.name "$LOGIN"
git config --global user.email >/dev/null || git config --global user.email "$(gh api user -q .id)+${LOGIN}@users.noreply.github.com"
git config --global init.defaultBranch main

# ---------- Repos ----------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || true)"
if [ -n "$SCRIPT_DIR" ] && [ -f "$SCRIPT_DIR/../syllabus.json" ]; then
  REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
  if ! git -C "$REPO_DIR" remote get-url origin >/dev/null 2>&1; then
    say "Creating your GitHub repos, milestones and issues (takes a few minutes)"
    bash "$REPO_DIR/scripts/setup.sh"
  fi
else
  REPO_DIR="${ML_JOURNEY_DIR:-$HOME/ml-journey}"
  if [ ! -d "$REPO_DIR/.git" ]; then
    say "Cloning github.com/$LOGIN/ml-journey to $REPO_DIR"
    gh repo clone "$LOGIN/ml-journey" "$REPO_DIR" \
      || fail "couldn't find github.com/$LOGIN/ml-journey. Ask Claude to create it, or run scripts/setup.sh from the starter zip."
  fi
fi
cd "$REPO_DIR"
git config pull.rebase true
git config core.hooksPath scripts/hooks

if [ ! -d private/.git ] && gh repo view "$LOGIN/ml-journey-private" >/dev/null 2>&1; then
  say "Cloning your private companion repo into private/"
  if [ -d private ] && [ -n "$(ls -A private 2>/dev/null)" ]; then mv private private.starter; fi
  gh repo clone "$LOGIN/ml-journey-private" private
fi
if [ -d private/.git ]; then
  mkdir -p private/.git/hooks && cp scripts/hooks/pre-commit private/.git/hooks/pre-commit
  git -C private config pull.rebase true
fi

# ---------- Python environment ----------
say "Building the Python environment (Python 3.12, PyTorch, MLX, Jupyter). First run downloads about 1 GB."
uv sync
uv run python -m ipykernel install --user --name ml-journey --display-name "ML Journey (Python 3.12)" >/dev/null

CODE="/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code"
if [ -x "$CODE" ]; then
  say "Adding VS Code extensions for Python and Jupyter"
  for ext in ms-python.python ms-toolsai.jupyter; do "$CODE" --install-extension "$ext" >/dev/null 2>&1 || true; done
fi

mkdir -p "$HOME/ml-data"

# ---------- Check and record ----------
say "Checking the environment and measuring your Mac's GPU"
uv run python scripts/check_env.py || true

git add ENVIRONMENT.md uv.lock 2>/dev/null || true
if ! git diff --cached --quiet; then
  git commit -q -m "Record my ML environment"
  git pull -q --rebase && git push -q && echo "Pushed ENVIRONMENT.md to GitHub."
fi

cat <<MSG

All set.
  Repo:      $REPO_DIR   (github.com/$LOGIN/ml-journey)
  Data:      ~/ml-data   (datasets and weights live here, outside git)
  Open:      code "$REPO_DIR"   then pick the "ML Journey (Python 3.12)" kernel in notebooks
  Run tests: cd "$REPO_DIR" && uv run pytest
  Add tools when a stage needs them, e.g.  uv sync --group llm
MSG
