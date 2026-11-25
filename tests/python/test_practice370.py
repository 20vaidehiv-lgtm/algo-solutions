import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice370 import Solution  # noqa: E402


class MaxProductSubarrayTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.maxProduct([10, 9, 1, 9, 8, -5, 0]), 6480)
        self.assertEqual(self.sol.maxProduct([1, 2, -8, -4, 8, -3, -1]), 1536)
        self.assertEqual(self.sol.maxProduct([1, 2, 3, 4, 5]), 120)
        self.assertEqual(self.sol.maxProduct([-1, 2]), 2)

    def test_single_negative_and_zeros(self):
        self.assertEqual(self.sol.maxProduct([-2]), -2)
        self.assertEqual(self.sol.maxProduct([-2, 0, -1]), 0)


if __name__ == "__main__":
    unittest.main()
