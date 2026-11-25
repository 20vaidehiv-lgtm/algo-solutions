import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice341 import Solution  # noqa: E402


class GenerateParenthesesTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(
            self.sol.generateParenthesis(3),
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        )
        self.assertEqual(self.sol.generateParenthesis(2), ["(())", "()()"])
        self.assertEqual(self.sol.generateParenthesis(1), ["()"])

    def test_zero(self):
        self.assertEqual(self.sol.generateParenthesis(0), [""])


if __name__ == "__main__":
    unittest.main()
