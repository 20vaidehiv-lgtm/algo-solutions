import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice314 import Solution  # noqa: E402


class GroupAnagramsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        res = self.sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        normalized = sorted([sorted(g) for g in res])
        expected = sorted([sorted(g) for g in [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]])
        self.assertEqual(normalized, expected)

    def test_single_and_empty(self):
        self.assertEqual(self.sol.groupAnagrams(["a"]), [["a"]])
        self.assertEqual(self.sol.groupAnagrams([""]), [[""]])


if __name__ == "__main__":
    unittest.main()
