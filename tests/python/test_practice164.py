import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice164 import Solution  # noqa: E402


class RemoveOuterParenthesesTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.removeOuterParentheses("(()())(())"), "()()()")
        self.assertEqual(sol.removeOuterParentheses("(()())(())(()(()))"), "()()()()(())")


if __name__ == "__main__":
    unittest.main()

