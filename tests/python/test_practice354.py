import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice354 import Solution  # noqa: E402


class ImplementAtoiTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.myAtoi("-999999999999"), -2147483648)
        self.assertEqual(self.sol.myAtoi("  -0012gfg4"), -12)
        self.assertEqual(self.sol.myAtoi("-123"), -123)

    def test_overflow_and_plus_sign(self):
        self.assertEqual(self.sol.myAtoi("999999999999"), 2147483647)
        self.assertEqual(self.sol.myAtoi("  +42abc"), 42)


if __name__ == "__main__":
    unittest.main()
