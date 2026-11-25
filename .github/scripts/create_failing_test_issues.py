#!/usr/bin/env python3
"""Automatically create GitHub issues for failing Python test cases."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SOLUTIONS_DIR = REPO_ROOT / "solutions"
TESTS_DIR = REPO_ROOT / "tests"

TEST_FILENAME_RE = re.compile(r"^test_(practice\d+)\.py$")
SOLUTION_FILENAME_RE = re.compile(r"^(practice\d+)\.[A-Za-z0-9]+$")


def run_git(*args: str) -> list[str]:
    """Execute a git command safely and return non-empty stripped output lines."""
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
    """Return True if sha exists locally and is not the all-zero null SHA."""
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


def get_changed_python_tests() -> list[Path]:
    """Resolve Python test files affected by changed solutions or tests."""
    before_sha = os.environ.get("BEFORE_SHA", "").strip()
    after_sha = os.environ.get("AFTER_SHA", "HEAD").strip() or "HEAD"

    changed_paths: set[str] = set()
    if is_valid_commit(before_sha) and is_valid_commit(after_sha):
        changed_paths.update(
            run_git("diff", "--name-only", "--diff-filter=AM", f"{before_sha}..{after_sha}", "--", "solutions/python/", "tests/python/")
        )
    else:
        parents = run_git("rev-list", "--parents", "-n", "1", "HEAD")
        is_merge = len(parents[0].split()) > 2 if parents else False
        if is_merge:
            changed_paths.update(
                run_git("diff", "--name-only", "--diff-filter=AM", "HEAD^1", "HEAD", "--", "solutions/python/", "tests/python/")
            )
        else:
            changed_paths.update(
                run_git("diff", "--name-only", "--diff-filter=AM", "HEAD~1", "HEAD", "--", "solutions/python/", "tests/python/")
            )

        if not changed_paths:
            changed_paths.update(
                run_git("show", "--name-only", "--diff-filter=AM", "--format=", "HEAD", "--", "solutions/python/", "tests/python/")
            )

    test_files: set[Path] = set()
    for rel in changed_paths:
        p = REPO_ROOT / rel
        if "__pycache__" in p.parts:
            continue
        if rel.startswith("tests/python/") and p.is_file() and TEST_FILENAME_RE.fullmatch(p.name):
            test_files.add(p)
        elif rel.startswith("solutions/python/") and p.is_file():
            match = SOLUTION_FILENAME_RE.fullmatch(p.name)
            if match:
                candidate = TESTS_DIR / "python" / f"test_{match.group(1)}.py"
                if candidate.is_file():
                    test_files.add(candidate)

    return sorted(test_files)


def extract_problem_name(solution_path: Path) -> str:
    """Extract the problem title from a solution header, falling back to stem."""
    if not solution_path.is_file():
        return solution_path.stem
    try:
        content = solution_path.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return solution_path.stem

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
    return solution_path.stem


def resolve_test_path(classname: str, test_name: str) -> Path | None:
    """
    Map a JUnit testcase's classname or name to tests/python/test_practice<n>.py.
    Collection errors leave classname empty and place the module name in test_name.
    """
    for raw in (classname, test_name):
        for part in (p for p in raw.split(".") if p):
            if TEST_FILENAME_RE.fullmatch(f"{part}.py"):
                candidate = TESTS_DIR / "python" / f"{part}.py"
                if candidate.is_file():
                    return candidate
    return None


def _parse_junit_xml(xml_path: Path, failures_by_file: dict[Path, list[dict[str, str]]]) -> bool:
    """Parse JUnit XML into failures_by_file; returns True if valid XML."""
    if not xml_path.is_file():
        return False
    try:
        tree = ET.parse(xml_path)
    except ET.ParseError as exc:
        print(f"Warning: Failed to parse JUnit XML report: {exc}", file=sys.stderr)
        return False

    for testcase in tree.getroot().iter("testcase"):
        failure_el = testcase.find("failure")
        error_el = testcase.find("error")
        issue_el = failure_el if failure_el is not None else error_el
        if issue_el is None:
            continue

        classname = testcase.attrib.get("classname", "")
        test_name = testcase.attrib.get("name", "unknown_test")
        test_file = resolve_test_path(classname, test_name)
        if test_file is None:
            continue

        message = (issue_el.attrib.get("message") or "").strip()
        detail = (issue_el.text or "").strip()
        if len(detail) > 600:
            detail = detail[-600:]

        failures_by_file[test_file].append({
            "test": test_name,
            "kind": "error" if error_el is not None else "failure",
            "message": message or "Test assertion failed",
            "detail": detail,
        })
    return True


def run_pytest_and_collect_failures(
    test_targets: list[Path],
    batch_timeout: int = 120,
    per_file_timeout: int = 15,
) -> dict[Path, list[dict[str, str]]]:
    """
    Run pytest with JUnit XML output and group failures/errors by test file.
    Falls back to per-file runs if the batch times out (e.g. due to an infinite loop).
    """
    if not test_targets:
        return {}

    failures_by_file: dict[Path, list[dict[str, str]]] = defaultdict(list)

    with tempfile.TemporaryDirectory() as tmpdir:
        xml_path = Path(tmpdir) / "pytest-results.xml"
        cmd = [
            sys.executable, "-m", "pytest",
            *[str(p) for p in test_targets],
            f"--junitxml={xml_path}",
            "--tb=short",
            "-q",
        ]
        try:
            subprocess.run(
                cmd,
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                timeout=batch_timeout,
            )
            if _parse_junit_xml(xml_path, failures_by_file):
                return dict(sorted(failures_by_file.items(), key=lambda kv: kv[0].name))
        except subprocess.TimeoutExpired:
            print(
                f"Batch pytest timed out after {batch_timeout}s; falling back to per-file isolation.",
                file=sys.stderr,
            )

        # Per-file fallback isolates any hanging test and still catches all other failures
        for idx, target in enumerate(test_targets):
            per_xml = Path(tmpdir) / f"result-{idx}.xml"
            per_cmd = [
                sys.executable, "-m", "pytest",
                str(target),
                f"--junitxml={per_xml}",
                "--tb=short",
                "-q",
            ]
            try:
                subprocess.run(
                    per_cmd,
                    cwd=REPO_ROOT,
                    capture_output=True,
                    text=True,
                    timeout=per_file_timeout,
                )
                _parse_junit_xml(per_xml, failures_by_file)
            except subprocess.TimeoutExpired:
                failures_by_file[target].append({
                    "test": target.stem,
                    "kind": "error",
                    "message": f"Test timed out after {per_file_timeout}s",
                    "detail": "Execution exceeded per-file timeout (possible infinite loop or blocking input).",
                })

    return dict(sorted(failures_by_file.items(), key=lambda kv: kv[0].name))


def fetch_open_issues(repo: str) -> list[dict[str, str]]:
    """Fetch open issues once to avoid repeated GitHub CLI calls per failing test."""
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
        data = json.loads(result.stdout)
        return data if isinstance(data, list) else []
    except Exception as exc:
        print(f"Warning: Could not list open issues: {exc}", file=sys.stderr)
        return []


def issue_already_exists(open_issues: list[dict[str, str]], solution_name: str, test_name: str) -> bool:
    """Return True if any open issue already mentions the exact solution or test filename."""
    sol_pat = re.compile(rf"(?<![A-Za-z0-9_]){re.escape(solution_name)}(?![A-Za-z0-9_.])", re.IGNORECASE)
    test_pat = re.compile(rf"(?<![A-Za-z0-9_]){re.escape(test_name)}(?![A-Za-z0-9_.])", re.IGNORECASE)
    for issue in open_issues:
        text = f"{issue.get('title', '')}\n{issue.get('body', '')}"
        if sol_pat.search(text) or test_pat.search(text):
            return True
    return False


def create_issue(
    test_path: Path,
    failures: list[dict[str, str]],
    repo: str,
    open_issues: list[dict[str, str]],
    dry_run: bool = False,
) -> bool:
    """Create a GitHub issue for a failing test file."""
    match = TEST_FILENAME_RE.fullmatch(test_path.name)
    if not match:
        return False

    stem = match.group(1)
    solution_path = SOLUTIONS_DIR / "python" / f"{stem}.py"
    solution_name = solution_path.name
    test_name = test_path.name
    rel_solution = solution_path.relative_to(REPO_ROOT).as_posix()
    rel_test = test_path.relative_to(REPO_ROOT).as_posix()

    problem = extract_problem_name(solution_path)
    problem_clean = re.sub(r'["`]', "'", problem).strip() or stem

    if not dry_run and issue_already_exists(open_issues, solution_name, test_name):
        print(f"Issue already exists for {solution_name} / {test_name}. Skipping.")
        return False

    title = f"Fix failing test for {problem_clean} ({solution_name})"

    failure_blocks = []
    for item in failures[:5]:
        block = f"- `{item['test']}` ({item['kind']}): `{item['message']}`"
        if item["detail"]:
            block += f"\n\n```text\n{item['detail']}\n```"
        failure_blocks.append(block)
    failures_md = "\n\n".join(failure_blocks)

    body = f"""\
## Fix failing test for `{problem_clean}`

Automated tests detected {len(failures)} failing case(s) for `{rel_solution}`.

**Solution:** [`{solution_name}`](https://github.com/{repo}/blob/main/{rel_solution})
**Test:** [`{test_name}`](https://github.com/{repo}/blob/main/{rel_test})
**Language:** python

### Failing Test(s)

{failures_md}

### Task

- [ ] Run `pytest {rel_test}` locally to reproduce the failure
- [ ] Inspect `{rel_solution}` and `{rel_test}` to see whether the bug is in the solution or the test expectation
- [ ] Fix the bug and verify `pytest {rel_test}` passes
- [ ] Open a Pull Request

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
"""

    if dry_run:
        print(f"[DRY RUN] Would create issue: {title}")
        return True

    labels = "bug,help wanted,good first issue,beginner-friendly"
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
        print(f"Error creating issue for {solution_name}: {exc}", file=sys.stderr)
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Create GitHub issues for failing Python tests.")
    parser.add_argument("--scope", choices=("auto", "changed", "all"), default="auto")
    parser.add_argument("--dry-run", action="store_true", help="Print issues without calling gh.")
    parser.add_argument("--max-issues", type=int, default=20, help="Cap issues created per run.")
    args = parser.parse_args()

    if args.max_issues < 1:
        print("ERROR: --max-issues must be at least 1.", file=sys.stderr)
        return 1

    repo = os.environ.get("GITHUB_REPOSITORY", "").strip()
    if not repo:
        if args.dry_run:
            repo = "Huerte/algo-solutions"
        else:
            print("ERROR: GITHUB_REPOSITORY env var is not set.", file=sys.stderr)
            return 1

    event_name = os.environ.get("EVENT_NAME", "").lower()
    scope = args.scope
    if scope == "auto":
        scope = "all" if event_name == "workflow_dispatch" else "changed"

    if scope == "all":
        targets = sorted(
            p for p in (TESTS_DIR / "python").glob("test_practice*.py")
            if p.is_file() and TEST_FILENAME_RE.fullmatch(p.name)
        )
    else:
        targets = get_changed_python_tests()

    if not targets:
        print("No Python test targets to run.")
        return 0

    print(f"Running pytest on {len(targets)} test file(s)...")
    failures_by_file = run_pytest_and_collect_failures(targets)

    if not failures_by_file:
        print("All targeted tests passed.")
        return 0

    print(f"Detected failing tests in {len(failures_by_file)} file(s).")
    open_issues = [] if args.dry_run else fetch_open_issues(repo)

    created = 0
    for test_path, failures in failures_by_file.items():
        if created >= args.max_issues:
            print(f"Reached max-issues limit ({args.max_issues}). Stopping.")
            break
        if create_issue(test_path, failures, repo, open_issues, dry_run=args.dry_run):
            created += 1

    print(f"Done. Processed {len(failures_by_file)} failing test file(s); created {created} issue(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
