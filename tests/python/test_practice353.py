import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice353 import Solution  # noqa: E402


class LongestPalindromeTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(
            self.sol.longestPalindrome("bswrhxboawtdfqggqfdtwyypwnssnwpyyaobxhrwsb"),
            "wtdfqggqfdtw",
        )
        self.assertEqual(self.sol.longestPalindrome("aaaabbaa"), "aabbaa")
        self.assertEqual(self.sol.longestPalindrome("ababa"), "ababa")

    def test_edge_cases(self):
        self.assertEqual(self.sol.longestPalindrome(""), "")
        self.assertEqual(self.sol.longestPalindrome("a"), "a")
        self.assertEqual(self.sol.longestPalindrome("cbbd"), "bb")


if __name__ == "__main__":
    unittest.main()
