import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice369 import Solution  # noqa: E402


class TwoSumPairTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertTrue(self.sol.twoSum([1, 2, 3, 4, 5], 9))
        self.assertFalse(self.sol.twoSum([1, 2, 3, 4, 5], 10))
        self.assertTrue(self.sol.twoSum([1, 2, 3, 4, 5], 5))

    def test_negatives_and_single(self):
        self.assertTrue(self.sol.twoSum([-3, 4, 1, 2], -1))
        self.assertFalse(self.sol.twoSum([5], 10))


if __name__ == "__main__":
    unittest.main()
