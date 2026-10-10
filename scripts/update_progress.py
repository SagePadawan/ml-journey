#!/usr/bin/env python3
"""Rebuild PROGRESS.md from GitHub milestones and the reading checkboxes in each stage README.

Runs in GitHub Actions (uses GITHUB_TOKEN and GITHUB_REPOSITORY). Run it locally without a
token to update only the reading counts.
"""
import json, os, re, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
stages = json.load(open(os.path.join(ROOT, "syllabus.json")))

def milestones():
    token, repo = os.environ.get("GITHUB_TOKEN"), os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        return {}
    out, page = {}, 1
    while True:
        req = urllib.request.Request(
            f"https://api.github.com/repos/{repo}/milestones?state=all&per_page=100&page={page}",
            headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"})
        with urllib.request.urlopen(req) as r:
            batch = json.load(r)
        for m in batch:
            out[m["title"]] = (m["closed_issues"], m["open_issues"] + m["closed_issues"])
        if len(batch) < 100:
            return out
        page += 1

def readings(folder):
    path = os.path.join(ROOT, folder, "README.md")
    if not os.path.exists(path):
        return 0, 0
    text = open(path).read()
    sec = text.split("## Readings", 1)[-1].split("\n## ", 1)[0]
    done = len(re.findall(r"^- \[[xX]\]", sec, re.M))
    total = done + len(re.findall(r"^- \[ \]", sec, re.M))
    return done, total

def bar(done, total, width=10):
    if not total:
        return "—"
    filled = round(width * done / total)
    return "█" * filled + "░" * (width - filled) + f" {done}/{total}"

ms = milestones()
rows, all_done, all_total, read_done, read_total = [], 0, 0, 0, 0
for st in stages:
    done, total = ms.get(st["milestone"], (0, len(st["project"]["ms"]) + 1))
    rd, rt = readings(st["folder"])
    all_done += done; all_total += total; read_done += rd; read_total += rt
    rows.append(f"| {st['label']} | [{st['name']}]({st['folder']}/) | {st['weeks'].replace('Weeks ', '')} | {bar(done, total)} | {bar(rd, rt)} |")

table = "\n".join([
    f"**Milestones:** {all_done} of {all_total} done · **Readings:** {read_done} of {read_total} done",
    "",
    "| # | Stage | Weeks | Milestones | Readings |",
    "|---|---|---|---|---|",
    *rows,
])
path = os.path.join(ROOT, "PROGRESS.md")
text = open(path).read()
new = re.sub(r"<!-- progress:start -->.*<!-- progress:end -->",
             "<!-- progress:start -->\n" + table + "\n<!-- progress:end -->", text, flags=re.S)
if new != text:
    open(path, "w").write(new)
    print("PROGRESS.md updated")
else:
    print("No change")
