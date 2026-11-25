---
name: Add a test
about: Add a test file for an existing solution that does not have one yet
title: "[Test]: Add test for practice<n> (<language>)"
labels: good first issue, help wanted, 5-minutes
---

## Which solution needs a test?

Link to the solution file on GitHub or give the filename (e.g. `solutions/python/practice42.py`).

## What should the test check?

Describe the cases you think are worth covering. If you are not sure, just say so, and a reviewer can help.

## Notes

Test files go in `tests/<language>/` and mirror the solution folder.
The naming convention matches the solution file exactly with a `test_` prefix:

| Language   | Solution                             | Test                                    |
|------------|--------------------------------------|-----------------------------------------|
| Python     | `solutions/python/practice42.py`     | `tests/python/test_practice42.py`       |
| JavaScript | `solutions/javascript/practice6.js`  | `tests/javascript/test_practice6.js`    |
| Java       | `solutions/java/practice5.java`      | `tests/java/test_practice5.java`        |

No prior test-writing experience needed. A maintainer will help review your test.
