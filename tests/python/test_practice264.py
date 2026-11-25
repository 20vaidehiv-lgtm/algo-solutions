import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice264 import Solution  # noqa: E402


class KadaneTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.maxSubarraySum([2, 3, -8, 7, -1, 2, 3]), 11)
        self.assertEqual(sol.maxSubarraySum([-3, -2, -6, -1, -7, -4]), -1)


if __name__ == "__main__":
    unittest.main()

