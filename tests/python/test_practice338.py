import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice338 import Solution  # noqa: E402


class MaximumSubarrayTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(self.sol.maxSubArray([5, 4, -1, 7, 8]), 23)
        self.assertEqual(self.sol.maxSubArray([1]), 1)

    def test_all_negative(self):
        self.assertEqual(self.sol.maxSubArray([-5, -2, -8, -1]), -1)


if __name__ == "__main__":
    unittest.main()
