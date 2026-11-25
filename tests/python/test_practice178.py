import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice178 import Solution  # noqa: E402


class FirstMatchingIndexTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_matches(self):
        self.assertEqual(self.sol.firstMatchingIndex("abcba"), 0)
        self.assertEqual(self.sol.firstMatchingIndex("abca"), 0)
        self.assertEqual(self.sol.firstMatchingIndex("abcbx"), 1)
        self.assertEqual(self.sol.firstMatchingIndex("abc"), 1)

    def test_no_match(self):
        self.assertEqual(self.sol.firstMatchingIndex("ab"), -1)
        self.assertEqual(self.sol.firstMatchingIndex(""), -1)


if __name__ == "__main__":
    unittest.main()
