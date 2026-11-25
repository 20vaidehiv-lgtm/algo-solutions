#!/usr/bin/env python3
"""Automatically create a GitHub issue when a solution with Status: IN PROGRESS is merged or pushed."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SOLUTIONS_DIR = REPO_ROOT / "solutions"

# Match comment lines that indicate in-progress / unfinished work
IN_PROGRESS_PATTERN = re.compile(
    r"^\s*(?:#|//|--|/\*+|\*|<!--)\s*(?:[^\w\s]\s*)?"
    r"(?:status\s*[:\-\u2014\u2013]?\s*.*)?"
    r"\b(in[-_\s]?progress|wip|work[-_\s]in[-_\s]progress|needs[-_\s]work|incomplete|unfinished|unsolved|todo)\b",
    re.IGNORECASE,
)

# Only treat Status lines explicitly marked done/solved (without in-progress keywords) as resolved
EXPLICIT_SOLVED_STATUS = re.compile(
    r"^\s*(?:#|//|--|/\*+|\*|<!--)\s*(?:[^\w\s]\s*)?status\s*[:\-\u2014\u2013]\s*"
    r"(?:[^\w\s]\s*)?(?:solved|done|complete|completed|passed|fixed)\b",
    re.IGNORECASE,
)

# Only files matching practice<n>.<ext> are managed solutions
SOLUTION_FILENAME = re.compile(r"^practice\d+\.[A-Za-z0-9]+$")


def run_git(*args: str) -> list[str]:
    """Execute git command safely and return stripped output lines."""
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        return [line.strip() for line in result.stdout.splitlines() if line.strip()]
    except subprocess.CalledProcessError as exc:
        print(f"Git command failed ('git {' '.join(args)}'): {exc}", file=sys.stderr)
        return []


def is_valid_commit(sha: str | None) -> bool:
    """Check if a commit SHA exists locally and is not a zero-hash."""
    if not sha or sha == "0" * 40 or not sha.strip():
        return False
    try:
        subprocess.run(
            ["git", "cat-file", "-e", f"{sha}^{{commit}}"],
            cwd=REPO_ROOT,
            capture_output=True,
            check=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def get_changed_solution_files(scan_all: bool = False) -> list[Path]:
    """
    Return added or modified solution files reliably across push ranges,
    merge commits (first parent only), or manual workflow dispatches.
    """
    event_name = os.environ.get("EVENT_NAME", "").lower()
    before_sha = os.environ.get("BEFORE_SHA", "").strip()
    after_sha = os.environ.get("AFTER_SHA", "HEAD").strip() or "HEAD"

    if scan_all or event_name == "workflow_dispatch":
        print("Scanning all solution files.")
        return sorted(
            f for f in SOLUTIONS_DIR.rglob("practice*.*")
            if f.is_file()
            and not f.name.startswith(".")
            and "__pycache__" not in f.parts
            and SOLUTION_FILENAME.fullmatch(f.name)
        )

    changed_names: set[str] = set()

    # 1. Push range diff (preferred: covers multi-commit pushes and merges accurately)
    if is_valid_commit(before_sha) and is_valid_commit(after_sha):
        print(f"Inspecting commit range: {before_sha[:8]}..{after_sha[:8]}")
        changed_names.update(
            run_git("diff", "--name-only", "--diff-filter=AM", f"{before_sha}..{after_sha}", "--", "solutions/")
        )
    else:
        # 2. Merge commit: diff ONLY against first parent (main before merge), never HEAD^2
        parents = run_git("rev-list", "--parents", "-n", "1", "HEAD")
        is_merge = len(parents[0].split()) > 2 if parents else False

        if is_merge:
            print("HEAD is a merge commit. Checking diff against first parent (HEAD^1..HEAD).")
            changed_names.update(run_git("diff", "--name-only", "--diff-filter=AM", "HEAD^1", "HEAD", "--", "solutions/"))
        else:
            # 3. Single commit fallback
            print("Inspecting HEAD~1..HEAD diff.")
            changed_names.update(run_git("diff", "--name-only", "--diff-filter=AM", "HEAD~1", "HEAD", "--", "solutions/"))

        # 4. Initial commit / shallow clone fallback
        if not changed_names:
            print("Falling back to HEAD commit metadata.")
            changed_names.update(run_git("show", "--name-only", "--diff-filter=AM", "--format=", "HEAD", "--", "solutions/"))

    files = []
    for name in changed_names:
        p = REPO_ROOT / name
        if (
            p.is_file()
            and not p.name.startswith(".")
            and "__pycache__" not in p.parts
            and SOLUTION_FILENAME.fullmatch(p.name)
        ):
            files.append(p)
    return sorted(files)


def is_in_progress(path: Path) -> bool:
    """
    Return True if the file's header contains an in-progress status marker.
    """
    try:
        content = path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return False

    for line in content.splitlines()[:30]:
        if IN_PROGRESS_PATTERN.search(line):
            return True
        if EXPLICIT_SOLVED_STATUS.search(line):
            return False
    return False


def extract_problem_name(path: Path) -> str:
    """Extract problem title from header or fall back to stem."""
    try:
        content = path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return path.stem

    for line in content.splitlines()[:25]:
        match = re.match(
            r"^\s*(?:#|//|--|/\*+|\*|<!--)\s*(?:[^\w\s]\s*)?problem(?:\s*[:\-\u2014\u2013]+\s*|\s+)(.*?)\s*(?:\*/|-->)?$",
            line,
            re.IGNORECASE,
        )
        if match:
            cleaned = re.sub(r"[\r\n\t]+", " ", match.group(1)).strip()
            cleaned = re.sub(r"\s*(?:\*/|-->)\s*$", "", cleaned).strip()
            if cleaned:
                return cleaned
    return path.stem


def fetch_open_issues(repo: str) -> list[dict[str, str]]:
    """Fetch open issues once per run to check for duplicates without N API calls."""
    try:
        result = subprocess.run(
            [
                "gh", "issue", "list",
                "--repo", repo,
                "--state", "open",
                "--limit", "500",
                "--json", "title,body",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        issues = json.loads(result.stdout)
        return issues if isinstance(issues, list) else []
    except Exception as exc:
        print(f"Warning: could not fetch open issues: {exc}", file=sys.stderr)
        return []


def issue_already_exists(open_issues: list[dict[str, str]], filename: str) -> bool:
    """Return True if an open issue already references the exact filename."""
    pat = re.compile(rf"(?<![A-Za-z0-9_]){re.escape(filename)}(?![A-Za-z0-9_.])", re.IGNORECASE)
    for issue in open_issues:
        text = f"{issue.get('title', '')}\n{issue.get('body', '')}"
        if pat.search(text):
            return True
    return False


def create_issue(
    path: Path,
    repo: str,
    open_issues: list[dict[str, str]],
    dry_run: bool = False,
) -> bool:
    filename = path.name
    rel_path = path.relative_to(REPO_ROOT).as_posix()
    lang = path.parent.name
    problem = extract_problem_name(path)

    problem_clean = re.sub(r'["`]', "'", problem).strip() or path.stem
    title = f"Fix and complete the {problem_clean} solution ({filename})"

    if not dry_run and issue_already_exists(open_issues, filename):
        print(f"Issue already exists for {filename}. Skipping.")
        return False

    body = f"""\
## Fix and complete the `{problem_clean}` solution

The file `{rel_path}` was merged with an in-progress status marker (`IN PROGRESS`, `WIP`, `TODO`, `NEEDS WORK`, or similar), which means the implementation is unfinished or has known issues.

**File:** [`{filename}`](https://github.com/{repo}/blob/main/{rel_path})
**Language:** {lang}

### Task

- [ ] Open `{rel_path}`
- [ ] Review the existing code and comments for what is incomplete or broken
- [ ] Fix or complete the implementation
- [ ] Remove the `Status: IN PROGRESS` marker and replace it with `Status: Done`
- [ ] Optionally add or update a test file at `tests/{lang}/test_{filename}` to cover your fix
- [ ] Open a Pull Request

No new solution file is needed. Fix the existing file in place.

---

## Open for everyone

This issue is open for everyone: beginners, experienced developers, students, and people who don't code at all. Any language, any level, no experience required. If you want to help, you are welcome here.

## How to contribute

1. Fork this repo
2. Clone your fork and create a new branch
3. Make your change
4. Commit, push, and open a Pull Request

New to open source? Start here:

**[Getting Started Guide](https://github.com/{repo}/blob/main/docs/GETTING_STARTED.md)**

Prefer video? Watch this: [How to contribute on GitHub (YouTube)](https://youtu.be/WldXhauP024?si=9u5wErqvnz9ZZRAv)

<!-- star-note -->
If this repo helps you or you like where it is going, a [star](https://github.com/{repo}) is a nice way to say thanks and helps other people find it. Entirely optional, and you do not need it to contribute.
"""

    if dry_run:
        print(f"[DRY RUN] Would create issue: {title}")
        return True

    labels = "bug,help wanted,good first issue,beginner-friendly,30-minutes"
    cmd = [
        "gh", "issue", "create",
        "--repo", repo,
        "--title", title,
        "--body", body,
        "--label", labels,
    ]
    print(f"Creating issue: {title}")
    try:
        subprocess.run(cmd, check=True)
        open_issues.append({"title": title, "body": body})
        return True
    except subprocess.CalledProcessError as exc:
        print(f"Error creating issue for {filename}: {exc}", file=sys.stderr)
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Create GitHub issues for in-progress solution files.")
    parser.add_argument("--all", action="store_true", help="Scan all solution files instead of git diff.")
    parser.add_argument("--dry-run", action="store_true", help="Print issues without calling gh.")
    args = parser.parse_args()

    repo = os.environ.get("GITHUB_REPOSITORY", "").strip()
    if not repo:
        if args.dry_run:
            repo = "Huerte/algo-solutions"
        else:
            print("ERROR: GITHUB_REPOSITORY env var is not set.", file=sys.stderr)
            return 1

    changed_files = get_changed_solution_files(scan_all=args.all)

    if not changed_files:
        print("No changed solution files detected.")
        return 0

    flagged = [f for f in changed_files if is_in_progress(f)]
    if not flagged:
        print("No in-progress solution files detected.")
        return 0

    print(f"Found {len(flagged)} in-progress file(s): {[f.name for f in flagged]}")
    open_issues = [] if args.dry_run else fetch_open_issues(repo)

    success_count = 0
    for file_path in flagged:
        if create_issue(file_path, repo, open_issues, dry_run=args.dry_run):
            success_count += 1

    print(f"Done. Created {success_count} issue(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
