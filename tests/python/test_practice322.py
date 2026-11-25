import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice322 import Solution  # noqa: E402


class DifferenceOfSumTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.differenceOfSum([1, 15, 6, 3]), 9)
        self.assertEqual(self.sol.differenceOfSum([1, 2, 3, 4]), 0)

    def test_multi_digit(self):
        self.assertEqual(self.sol.differenceOfSum([10, 20]), 27)


if __name__ == "__main__":
    unittest.main()
