import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice409 import is_valid  # noqa: E402


class ValidParenthesesTest(unittest.TestCase):
    def test_cases(self):
        self.assertTrue(is_valid("()"))
        self.assertTrue(is_valid("()[]{}"))
        self.assertFalse(is_valid("(]"))
        self.assertTrue(is_valid("([])"))
        self.assertFalse(is_valid("([)]"))
        self.assertTrue(is_valid(""))


if __name__ == "__main__":
    unittest.main()

