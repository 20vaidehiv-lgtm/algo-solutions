#!/usr/bin/env python3
"""Validate the required metadata header in changed solution files."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Problem and Source are always required.
# Third field: Note OR Topic (at least one, non-empty).
REQUIRED_FIELDS = ("Problem", "Source")
THIRD_FIELD_ALTERNATIVES = ("Note", "Topic")

# Matches any supported comment prefix followed by field: value
# s? handles plural "Topics:"
HEADER_PATTERN = r"^\s*(?:#|//|--|/\*+|\*|<!--)\s*{field}s?\s*:\s*(.*?)\s*(?:\*/|-->)?\s*$"
SOLUTION_FILENAME = re.compile(r"^practice\d+\.[A-Za-z0-9]+$")
IGNORED_SUFFIXES = {".pyc", ".pyo", ".pyd", ".class", ".o", ".out", ".exe"}


def is_valid_commit(sha: str) -> bool:
    """Return True if sha resolves to an existing git commit."""
    if not sha or sha == "0" * 40 or not sha.strip():
        return False
    try:
        subprocess.run(
            ["git", "cat-file", "-e", f"{sha}^{{commit}}"],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False


def run_diff_cmd(args: list[str]) -> list[Path] | None:
    """Execute git diff safely and return matching solution paths, or None on error."""
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
        )
        paths = (
            item.decode("utf-8", errors="surrogateescape")
            for item in result.stdout.split(b"\0")
            if item
        )
        return [REPO_ROOT / path for path in paths if path.startswith("solutions/")]
    except subprocess.CalledProcessError:
        return None


def changed_solution_files(base: str, head: str) -> list[Path]:
    """Return added, copied, modified, and renamed solution paths in a diff with fallbacks."""
    seen: set[Path] = set()

    def _dedupe(paths: list[Path]) -> list[Path]:
        unique: list[Path] = []
        for p in paths:
            if p not in seen:
                seen.add(p)
                unique.append(p)
        return unique

    # 1. When both base and head are valid commits, trust their diff (no fallback to HEAD~1).
    if is_valid_commit(base) and is_valid_commit(head):
        paths = run_diff_cmd(["diff", "--name-only", "-z", "--diff-filter=ACMR", f"{base}...{head}", "--", "solutions/"])
        if paths is not None:
            return _dedupe(paths)

        paths = run_diff_cmd(["diff", "--name-only", "-z", "--diff-filter=ACMR", f"{base}..{head}", "--", "solutions/"])
        if paths is not None:
            return _dedupe(paths)

    # 2. Fallback: HEAD~1..HEAD
    paths = run_diff_cmd(["diff", "--name-only", "-z", "--diff-filter=ACMR", "HEAD~1", "HEAD", "--", "solutions/"])
    if paths is not None:
        return _dedupe(paths)

    # 3. Final fallback: show files in HEAD commit (for initial commit / shallow clone)
    paths = run_diff_cmd(["show", "-z", "--name-only", "--diff-filter=ACMR", "--format=", "HEAD", "--", "solutions/"])
    if paths is not None:
        return _dedupe(paths)

    return []


def should_ignore_path(path: Path) -> bool:
    """Return True for non-solution metadata/build files (dotfiles, __pycache__, binaries)."""
    if not path.is_file():
        return True
    if path.name.startswith(".") or "__pycache__" in path.parts:
        return True
    if path.suffix.lower() in IGNORED_SUFFIXES:
        return True
    return False


def validate_file(path: Path) -> list[str]:
    """Return validation errors for a single solution file."""
    if should_ignore_path(path):
        return []

    errors: list[str] = []

    if not SOLUTION_FILENAME.fullmatch(path.name):
        errors.append(
            f"filename '{path.name}' must match practice<n>.<ext> "
            "(e.g. practice42.py)"
        )

    try:
        with path.open("r", encoding="utf-8-sig", errors="replace") as fh:
            top_lines = [fh.readline().rstrip("\r\n") for _ in range(30)]
    except (OSError, UnicodeError) as error:
        return [f"could not read file: {error}"]

    for field in REQUIRED_FIELDS:
        pattern = re.compile(HEADER_PATTERN.format(field=re.escape(field)), re.IGNORECASE)
        found = any(
            (m := pattern.match(line)) and m.group(1).strip()
            for line in top_lines
        )
        if not found:
            errors.append(
                f"missing or empty '{field}:' header "
                "(supported prefixes: #, //, --, /*, *, or <!--)"
            )

    # At least one of Note or Topic must be present and non-empty
    third_found = False
    for field in THIRD_FIELD_ALTERNATIVES:
        pattern = re.compile(HEADER_PATTERN.format(field=re.escape(field)), re.IGNORECASE)
        if any(
            (m := pattern.match(line)) and m.group(1).strip()
            for line in top_lines
        ):
            third_found = True
            break

    if not third_found:
        errors.append(
            "missing or empty 'Note:' or 'Topic:' header - include at least one "
            "(supported prefixes: #, //, --, /*, *, or <!--)"
        )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check metadata headers in solution files changed by a pull request."
    )
    parser.add_argument("--base", default="", help="Base commit SHA")
    parser.add_argument("--head", default="", help="Head commit SHA")
    args = parser.parse_args()

    files = changed_solution_files(args.base, args.head)
    # Check all changed non-ignored files under solutions/ so misnamed solution files are caught
    candidate_files = [f for f in files if not should_ignore_path(f)]

    if not candidate_files:
        print("No solution files changed; header validation skipped.")
        return 0

    failures: dict[Path, list[str]] = {}
    for path in candidate_files:
        errs = validate_file(path)
        if errs:
            failures[path] = errs

    if failures:
        print(f"Header validation failed for {len(failures)} file(s):\n")
        for path, errs in sorted(failures.items(), key=lambda kv: str(kv[0])):
            try:
                rel = path.relative_to(REPO_ROOT)
            except ValueError:
                rel = path
            print(f"  {rel}")
            for err in errs:
                print(f"    - {err}")
        print(
            "\nRequired header format (top of file):\n"
            "  # Problem: Two Sum\n"
            "  # Source: https://leetcode.com/problems/two-sum\n"
            "  # Topic: Hash Table, Arrays   <- OR  # Note: Used a dict for O(n) lookup"
        )
        return 1

    print(f"All headers valid -- {len(candidate_files)} changed solution file(s) checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
