#!/usr/bin/env python3
"""Create labels, milestones (with due dates) and one issue per project milestone.

Safe to re-run: anything that already exists is skipped.
Usage: python3 scripts/create_issues.py [--start YYYY-MM-DD] [--dry-run]
"""
import datetime as dt, json, os, re, subprocess, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
stages = json.load(open(os.path.join(ROOT, "syllabus.json")))
DRY = "--dry-run" in sys.argv

def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default

today = dt.date.today()
start = dt.date.fromisoformat(arg("--start") or (today + dt.timedelta(days=(7 - today.weekday()) % 7 or 7)).isoformat())

COLORS = {"0": "6b7486", "1": "8a5a2b", "2": "6b7500", "3": "2a62d4", "4": "7b4bb3", "5": "b8336f", "6": "2f7d1f",
          "7": "0b84a0", "8": "b26b00", "9": "4d6b8a", "10": "cf3f33", "A": "d4570b", "B": "8f1d3f", "C": "283c8f", "D": "007f78", "S": "4b2aa8"}

def gh(*args, data=None):
    if DRY:
        print("gh", " ".join(args))
        return "[]"
    for attempt in range(4):
        r = subprocess.run(["gh", *args], input=data, capture_output=True, text=True)
        if r.returncode == 0:
            return r.stdout
        if "rate limit" in r.stderr.lower() or "secondary" in r.stderr.lower():
            time.sleep(30 * (attempt + 1)); continue
        raise SystemExit(f"gh {' '.join(args)} failed:\n{r.stderr}")
    raise SystemExit("Hit GitHub rate limits; wait a few minutes and re-run. Nothing is duplicated.")

repo = "OWNER/REPO" if DRY else gh("repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner").strip()
print(f"Repo: {repo}  ·  Week 1 starts {start}")

def lines(path, jq):
    if DRY:
        return []
    out = gh("api", "--paginate", path, "--jq", jq)
    return [x for x in out.splitlines() if x.strip()]

existing_labels = set(lines(f"repos/{repo}/labels?per_page=100", ".[].name"))
existing_ms = {}
for row in lines(f"repos/{repo}/milestones?state=all&per_page=100", '.[] | "\\(.number)\\t\\(.title)"'):
    num, title = row.split("\t", 1)
    existing_ms[title] = int(num)
existing_issues = set(lines(f"repos/{repo}/issues?state=all&per_page=100", ".[] | select(.pull_request == null) | .title"))

for name, color, desc in [("project", "1d3a6b", "Project milestone"), ("reflection", "5a6475", "Explain back and revisit")]:
    if name not in existing_labels:
        gh("api", f"repos/{repo}/labels", "-f", f"name={name}", "-f", f"color={color}", "-f", f"description={desc}")

created = 0
for st in stages:
    key = st["code"] or str(st["n"])
    label = f"track-{key.lower()}" if st["code"] else f"stage-{key}"
    short = f"T{key}" if st["code"] else f"S{key}"
    if label not in existing_labels:
        gh("api", f"repos/{repo}/labels", "-f", f"name={label}", "-f", f"color={COLORS[key]}", "-f", f"description={st['milestone']}")
    end_week = int(re.findall(r"\d+", st["weeks"])[-1])
    due = start + dt.timedelta(days=7 * end_week - 1)
    if st["milestone"] not in existing_ms:
        out = gh("api", f"repos/{repo}/milestones", "-f", f"title={st['milestone']}",
                 "-f", f"description={st['weeks']} · {st['project']['title']}", "-f", f"due_on={due.isoformat()}T23:59:59Z")
        existing_ms[st["milestone"]] = 0 if DRY else json.loads(out)["number"]
    num = existing_ms[st["milestone"]]
    link = f"{st['folder']}/README.md"
    items = [(f"[{short}] {m}", "project", m) for m in st["project"]["ms"]]
    items.append((f"[{short}] Explain back and revisit", "reflection", None))
    for title, kind, m in items:
        title = title if len(title) <= 240 else title[:237] + "…"
        if title in existing_issues:
            continue
        if kind == "project":
            body = (f"**{st['milestone']}** · {st['project']['title']}\n\n{m}\n\n"
                    f"- [ ] Prediction written in [{link}](../blob/main/{link}) before running\n"
                    f"- [ ] Code committed to `{st['folder']}/code/`\n"
                    f"- [ ] Plot or table saved to `{st['folder']}/results/`\n"
                    f"- [ ] Results row filled in; big misses logged in ERRORS.md\n\n"
                    f"Close this issue from a commit message: `Closes #<this issue number>`.")
        else:
            body = (f"**{st['milestone']}**\n\n**Explain back:** {st['explain']}\n\n**Revisit:** {st['revisit']}\n\n"
                    f"Write both in [{link}](../blob/main/{link}), then close this issue.")
        gh("api", f"repos/{repo}/issues", "-f", f"title={title}", "-f", f"body={body}",
           "-F", f"milestone={num}", "-f", f"labels[]={label}", "-f", f"labels[]={kind}")
        created += 1
        if not DRY:
            time.sleep(1.2)
    print(f"  {st['milestone']}: ready")
print(f"Done. Created {created} issues.")
