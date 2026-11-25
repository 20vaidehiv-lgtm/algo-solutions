import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice349 import Solution  # noqa: E402


class LongestSubarraySumKTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.longestSubarray([10, 5, 2, 7, 1, -10], 15), 6)
        self.assertEqual(self.sol.longestSubarray([-5, 8, -14, 2, 4, 12], -5), 5)
        self.assertEqual(self.sol.longestSubarray([1, 2, 3, 4, 5], 15), 5)

    def test_no_match_and_zeros(self):
        self.assertEqual(self.sol.longestSubarray([1, 2, 3], 10), 0)
        self.assertEqual(self.sol.longestSubarray([0, 0, 0, 5], 5), 4)


if __name__ == "__main__":
    unittest.main()
