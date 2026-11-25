import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice316 import Solution  # noqa: E402


class WildcardMatchingTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertFalse(self.sol.isMatch("aa", "a"))
        self.assertTrue(self.sol.isMatch("aa", "*"))
        self.assertFalse(self.sol.isMatch("cb", "?a"))
        self.assertTrue(self.sol.isMatch("adceb", "*a*b"))

    def test_empty(self):
        self.assertTrue(self.sol.isMatch("", ""))
        self.assertTrue(self.sol.isMatch("", "***"))


if __name__ == "__main__":
    unittest.main()
