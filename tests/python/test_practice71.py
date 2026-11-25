import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice71 import is_valid_parentheses  # noqa: E402


class ValidParenthesesTest(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(is_valid_parentheses("()[]{}"))
        self.assertFalse(is_valid_parentheses("(]"))
        self.assertTrue(is_valid_parentheses(""))


if __name__ == "__main__":
    unittest.main()

