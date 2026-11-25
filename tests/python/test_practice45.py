import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice45 import Solution  # noqa: E402


class ValidParenthesesTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertTrue(sol.isValid("()[]{}"))
        self.assertFalse(sol.isValid("({{{{}}}))"))
        self.assertFalse(sol.isValid("(]"))


if __name__ == "__main__":
    unittest.main()

