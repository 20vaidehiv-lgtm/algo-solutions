import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice137 import valid_parenthesis  # noqa: E402


class ValidParenthesisTest(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(valid_parenthesis("{[()]}"))
        self.assertFalse(valid_parenthesis("({)}"))
        self.assertFalse(valid_parenthesis("{([])}][]"))

    def test_basic_and_empty(self):
        self.assertTrue(valid_parenthesis(""))
        self.assertTrue(valid_parenthesis("()[]{}"))


if __name__ == "__main__":
    unittest.main()
