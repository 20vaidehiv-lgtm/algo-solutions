# Contributing to Programming Problem Solving

Welcome! First off, thank you for considering contributing to this repository. 

This project is **open to everyone**: complete beginners, students, experienced developers, and people who don't write code at all. Whether this is your 100th pull request or your very first one, you are welcome here!

---

## New to Open Source?

If you have never used Git or GitHub before, read this first:

- **[Getting Started Guide](docs/GETTING_STARTED.md)**: a step-by-step walkthrough written for complete beginners. It covers installing Git, creating a GitHub account, forking, cloning, branching, committing, pushing, and opening your first Pull Request. No prior experience needed.

If you prefer to watch instead of read:
- **Video Walkthrough:** [How to contribute on GitHub (YouTube)](https://youtu.be/WldXhauP024?si=9u5wErqvnz9ZZRAv)

---

## Quick Contribution Steps

1. **Claim an issue:** Browse the [open issues](https://github.com/Huerte/algo-solutions/issues) and leave a comment on the one you want to work on so nobody else starts the same thing.
2. **Fork the repo:** Click the **Fork** button at the top-right of this repository to create your own copy.
3. **Create a branch:** Clone your fork locally (or use the GitHub website directly) and create a new branch for your changes.
4. **Make your change:** Add your solution, documentation, or improvement.
5. **Open a Pull Request:** Commit your changes, push them to your fork, and open a Pull Request back to this repository.

---

## 1. How to Name and Place a Solution File

Solutions are organized inside the `solutions/` directory by programming language, and numbered in the order they are added:

```text
algo-solutions/
├── solutions/
│   ├── python/
│   │   ├── practice1.py
│   │   ├── practice2.py
│   │   └── ...
│   └── javascript/
│       └── practice1.js
└── tests/
    ├── python/
    │   └── test_practice1.py      ← optional, but encouraged
    ├── javascript/
    │   └── test_practice1.js
    └── java/
        └── test_practice1.java
```

### Rules for placing and naming your file:
- **Folder path:** Place your solution in `solutions/<language>/practice<next_number>.<ext>`.
- **Lowercase folder names:** Always use a lowercase name for the language folder (e.g., `python`, `javascript`, `typescript`, `java`, `cpp`, `c`, `csharp`, `go`, `rust`, `kotlin`, `swift`, `php`, `ruby`).
- **File numbering:** Look inside the language folder to find the highest `practice<n>` number currently there, and add `1`. 
  - *Example:* If the highest file in `solutions/python/` is `practice408.py`, name your new file `practice409.py`.
- **Adding a new language:** Don't see a folder for your language yet? Create it and name your file `practice1.<ext>` (for example, `solutions/javascript/practice1.js`). You'll be the very first contributor for that language!

---

## 2. Adding a Test File (Optional but Encouraged)

Test files live in `tests/<language>/` — mirroring the solution folder. This keeps everything tidy and consistent across all languages.

### Naming convention

| Language | Solution | Test |
|---|---|---|
| Python | `solutions/python/practice42.py` | `tests/python/test_practice42.py` |
| JavaScript | `solutions/javascript/practice6.js` | `tests/javascript/test_practice6.js` |
| Java | `solutions/java/practice5.java` | `tests/java/test_practice5.java` |

### Python test template

```python
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice42 import your_function  # noqa: E402


class YourFunctionTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(your_function([1, 2, 3]), expected_result)


if __name__ == "__main__":
    unittest.main()
```

> Test files are optional. You do not need one to get a PR merged. But adding one earns you bonus points and helps everyone who reads the solution later.

---

## 3. Header Comment Format

Every solution file must start with a header comment at the very top that includes:
1. **Problem:** The name of the problem.
2. **Source:** A direct link to the problem (LeetCode, Codewars, HackerRank, CheckiO, GeeksforGeeks, etc.).
3. **Note** or **Topic:** Either a short note about your approach, or the topic/category tags — at least one of the two.

### Python Example (`#`):
```python
# Problem: Two Sum
# Source: https://leetcode.com/problems/two-sum
# Topic: Hash Table, Arrays
```

Or with Note instead:
```python
# Problem: Two Sum
# Source: https://leetcode.com/problems/two-sum
# Note: Used a dictionary for O(n) lookup
```

### JavaScript / C++ / Java / Go / Rust Example (`//`):
```javascript
// Problem: Two Sum
// Source: https://leetcode.com/problems/two-sum
// Topic: Hash Table, Arrays
```

---

## 4. How to Run or Check Your Solution Before Submitting

Before opening your Pull Request, please make sure your code runs without syntax errors and solves the problem:

1. **Test on the problem platform:** Run your code against the test cases on the original site (such as LeetCode, Codewars, or HackerRank) to verify that it passes.
2. **Run it locally (or in an online runner):** Double-check that your file runs cleanly on its own without crashing. For example:
   - **Python:** `python solutions/python/practice<n>.py`
   - **JavaScript:** `node solutions/javascript/practice<n>.js`
3. **Run your test file (if you wrote one):**
   - **Python:** `python -m pytest tests/python/test_practice<n>.py`
   - **JavaScript:** `node tests/javascript/test_practice<n>.js`
4. **Don't stress about perfection:** Messy but working code is completely welcome! If anything can be improved or cleaned up, we will gladly help polish it together during code review.

---

## 5. What a Good Pull Request Title Looks Like

A good PR title is short, clear, and tells reviewers what you did at a glance.

### Good PR Title Examples:
- `Add Python solution for Two Sum (practice409)`
- `Add JavaScript solution for Valid Palindrome (practice1)`
- `Add test for Trap Rain Water (practice423)`
- `Docs: Add CONTRIBUTING.md for new contributors`
- `Fix typo in README.md`

### Less Helpful PR Titles (Try to Avoid):
- `Update file`
- `My first PR`
- `Fixed issue`

**Tip for PR Descriptions:** In the description box of your Pull Request, include `Closes #<issue-number>` (for example, `Closes #142`) so GitHub automatically links your PR to the issue!

---

## 6. Where to Ask for Help

Stuck on a git command, unsure where a file goes, or confused by a review comment? **Please ask!**

- **On an Issue:** Leave a comment directly on the issue you are working on.
- **On a Pull Request:** Leave a comment on your open Pull Request if you get stuck midway through.
- **General Questions:** Open a new [Issue](https://github.com/Huerte/algo-solutions/issues) with your question.

Basic questions are always fine, everyone starts somewhere, and we are happy to help you through your contribution!
