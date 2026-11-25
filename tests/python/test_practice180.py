import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice180 import Solution  # noqa: E402


class SortedSquaresTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.sortedSquares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
        self.assertEqual(self.sol.sortedSquares([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])

    def test_edge_cases(self):
        self.assertEqual(self.sol.sortedSquares([]), [])
        self.assertEqual(self.sol.sortedSquares([-5, -2, -1]), [1, 4, 25])


if __name__ == "__main__":
    unittest.main()
