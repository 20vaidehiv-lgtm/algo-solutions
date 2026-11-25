import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice325 import Solution  # noqa: E402


class PrefixCountTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.prefixCount(["leetcode", "win", "loops", "success"], "code"), 0)
        self.assertEqual(self.sol.prefixCount(["pay", "attention", "practice", "attend"], "at"), 2)

    def test_empty_prefix(self):
        self.assertEqual(self.sol.prefixCount(["a", "ab", "abc"], ""), 3)


if __name__ == "__main__":
    unittest.main()
