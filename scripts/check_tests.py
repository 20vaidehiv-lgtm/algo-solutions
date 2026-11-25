#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import platform
import re
import signal
import subprocess
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOLUTION_FILENAME = re.compile(r"^practice\d+\.[A-Za-z0-9]+$")
IGNORED_SUFFIXES = {".pyc", ".pyo", ".pyd", ".class", ".o", ".out", ".exe"}

TEST_TIMEOUT_SECONDS = 30
COMPILE_TIMEOUT_SECONDS = 60


def is_valid_commit(sha: str) -> bool:
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
    seen: set[Path] = set()

    def _dedupe(paths: list[Path]) -> list[Path]:
        unique: list[Path] = []
        for p in paths:
            if p not in seen:
                seen.add(p)
                unique.append(p)
        return unique

    if is_valid_commit(base) and is_valid_commit(head):
        paths = run_diff_cmd(["diff", "--name-only", "-z", "--diff-filter=ACMR", f"{base}...{head}", "--", "solutions/"])
        if paths is not None:
            return _dedupe(paths)
        paths = run_diff_cmd(["diff", "--name-only", "-z", "--diff-filter=ACMR", f"{base}..{head}", "--", "solutions/"])
        if paths is not None:
            return _dedupe(paths)

    paths = run_diff_cmd(["diff", "--name-only", "-z", "--diff-filter=ACMR", "HEAD~1", "HEAD", "--", "solutions/"])
    if paths is not None:
        return _dedupe(paths)

    paths = run_diff_cmd(["show", "-z", "--name-only", "--diff-filter=ACMR", "--format=", "HEAD", "--", "solutions/"])
    if paths is not None:
        return _dedupe(paths)

    return []


def lang_from_path(solution: Path) -> str | None:
    parts = solution.relative_to(REPO_ROOT).parts
    return parts[1] if len(parts) >= 2 else None


def expected_test_file(solution: Path) -> Path:
    lang = lang_from_path(solution)
    test_name = f"test_{solution.stem}{solution.suffix}"
    return REPO_ROOT / "tests" / lang / test_name


def _kill_process_tree(proc: subprocess.Popen) -> None:
    if platform.system() == "Windows":
        subprocess.run(["taskkill", "/PID", str(proc.pid), "/T", "/F"], capture_output=True)
    else:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        except ProcessLookupError:
            pass


def _run(
    cmd: list[str],
    cwd: Path | None = None,
    env: dict | None = None,
    timeout: int = TEST_TIMEOUT_SECONDS,
) -> tuple[int, str]:
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)

    popen_kwargs: dict = dict(
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=merged_env,
        cwd=str(cwd or REPO_ROOT),
        start_new_session=True,
    )

    with subprocess.Popen(cmd, **popen_kwargs) as proc:
        try:
            stdout, stderr = proc.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            _kill_process_tree(proc)
            try:
                stdout, stderr = proc.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                stdout, stderr = "", ""
            partial = (stdout + stderr).strip()
            timeout_msg = (
                f"[TIMEOUT] Process exceeded {timeout}s and was killed.\n"
                + (f"Partial output:\n{partial}" if partial else "No output captured.")
            )
            return -1, timeout_msg

    return proc.returncode, (stdout + stderr).strip()


def run_python(test_file: Path) -> tuple[bool, str]:
    code, out = _run(["python", "-m", "pytest", str(test_file), "-v", "--tb=short"])
    return code == 0, out


def run_javascript(test_file: Path) -> tuple[bool, str]:
    code, out = _run(["node", str(test_file)])
    return code == 0, out


def run_typescript(test_file: Path) -> tuple[bool, str]:
    code, out = _run(["node", "--experimental-strip-types", str(test_file)])
    return code == 0, out


def run_java(test_file: Path) -> tuple[bool, str]:
    stem = test_file.stem[len("test_"):]
    solution_file = REPO_ROOT / "solutions" / "java" / f"{stem}.java"
    solution_dir = solution_file.parent

    with tempfile.TemporaryDirectory() as tmp:
        classpath = f"{solution_dir}{os.pathsep}{test_file.parent}{os.pathsep}{tmp}"
        code, out = _run(
            ["javac", "-cp", classpath, "-d", tmp, str(solution_file), str(test_file)],
            timeout=COMPILE_TIMEOUT_SECONDS,
        )
        if code != 0:
            return False, f"Compilation failed:\n{out}"
        code, out = _run(["java", "-cp", tmp, test_file.stem], timeout=TEST_TIMEOUT_SECONDS)
        return code == 0, out


def run_cpp(test_file: Path) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory() as tmp:
        binary = Path(tmp) / "test_binary"
        code, out = _run(
            ["g++", "-std=c++17", str(test_file), "-o", str(binary)],
            timeout=COMPILE_TIMEOUT_SECONDS,
        )
        if code != 0:
            return False, f"Compilation failed:\n{out}"
        code, out = _run([str(binary)], timeout=TEST_TIMEOUT_SECONDS)
        return code == 0, out


def run_c(test_file: Path) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory() as tmp:
        binary = Path(tmp) / "test_binary"
        code, out = _run(
            ["gcc", str(test_file), "-o", str(binary)],
            timeout=COMPILE_TIMEOUT_SECONDS,
        )
        if code != 0:
            return False, f"Compilation failed:\n{out}"
        code, out = _run([str(binary)], timeout=TEST_TIMEOUT_SECONDS)
        return code == 0, out


def run_haskell(test_file: Path) -> tuple[bool, str]:
    code, out = _run(["runghc", str(test_file)])
    return code == 0, out


RUNNERS: dict[str, callable] = {
    "python":     run_python,
    "javascript": run_javascript,
    "typescript": run_typescript,
    "java":       run_java,
    "cpp":        run_cpp,
    "c":          run_c,
    "haskell":    run_haskell,
}


def should_ignore(path: Path) -> bool:
    if not path.is_file():
        return True
    if path.name.startswith(".") or "__pycache__" in path.parts:
        return True
    return path.suffix.lower() in IGNORED_SUFFIXES


def _indent(text: str, spaces: int) -> str:
    pad = " " * spaces
    return "\n".join(pad + line for line in text.splitlines())


def validate_solution(solution: Path) -> list[str]:
    errors: list[str] = []

    if not SOLUTION_FILENAME.fullmatch(solution.name):
        return errors

    lang = lang_from_path(solution)
    if lang is None:
        errors.append("could not determine language from path")
        return errors

    test_file = expected_test_file(solution)

    if not test_file.exists():
        errors.append(
            f"missing test file: expected '{test_file.relative_to(REPO_ROOT)}'. "
            "Every new solution must include an assertion test file."
        )
        return errors

    runner = RUNNERS.get(lang)
    if runner is None:
        errors.append(
            f"no test runner configured for language '{lang}'. "
            "Add one to scripts/check_tests.py::RUNNERS."
        )
        return errors

    passed, output = runner(test_file)
    if not passed:
        errors.append(
            f"test '{test_file.relative_to(REPO_ROOT)}' FAILED for "
            f"'{solution.relative_to(REPO_ROOT)}'.\n"
            f"    Output:\n{_indent(output, 6)}"
        )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check that changed solution files have passing tests."
    )
    parser.add_argument("--base", default="", help="Base commit SHA")
    parser.add_argument("--head", default="", help="Head commit SHA")
    args = parser.parse_args()

    files = changed_solution_files(args.base, args.head)
    candidates = [f for f in files if not should_ignore(f)]

    if not candidates:
        print("No solution files changed; test validation skipped.")
        return 0

    failures: dict[Path, list[str]] = {}
    for path in candidates:
        errs = validate_solution(path)
        if errs:
            failures[path] = errs

    if failures:
        print(f"Test validation failed for {len(failures)} file(s):\n")
        for path, errs in sorted(failures.items(), key=lambda kv: str(kv[0])):
            try:
                rel = path.relative_to(REPO_ROOT)
            except ValueError:
                rel = path
            print(f"  {rel}")
            for err in errs:
                print(f"    - {err}")
        print(
            "\nFix guide:\n"
            "  1. Add tests/<lang>/test_<filename> with at least one assertion.\n"
            "  2. Run it locally before pushing:\n"
            "       Python:     python -m pytest tests/python/test_practiceN.py\n"
            "       JavaScript: node tests/javascript/test_practiceN.js\n"
            "       C++:        g++ -std=c++17 tests/cpp/test_practiceN.cpp -o /tmp/t && /tmp/t\n"
            "       Java:       javac solutions/java/practiceN.java tests/java/test_practiceN.java\n"
            "                   java -cp . test_practiceN\n"
            f"  3. Tests exceeding {TEST_TIMEOUT_SECONDS}s are killed (infinite loop / freeze guard).\n"
        )
        return 1

    print(f"All tests passed -- {len(candidates)} changed solution file(s) checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
