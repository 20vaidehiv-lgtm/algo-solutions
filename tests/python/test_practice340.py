import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice340 import Solution  # noqa: E402


class SpiralMatrixIITest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(
            self.sol.generateMatrix(4),
            [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]],
        )
        self.assertEqual(
            self.sol.generateMatrix(3),
            [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
        )
        self.assertEqual(self.sol.generateMatrix(1), [[1]])

    def test_size_two(self):
        self.assertEqual(self.sol.generateMatrix(2), [[1, 2], [4, 3]])


if __name__ == "__main__":
    unittest.main()
