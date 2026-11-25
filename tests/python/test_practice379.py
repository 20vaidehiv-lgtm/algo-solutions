import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice379 import Solution  # noqa: E402


class SpiralOrderTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(
            self.solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        )
        self.assertEqual(
            self.solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        )
        self.assertEqual(
            self.solution.spiralOrder([[1, 2, 3], [4, 5, 6]]),
            [1, 2, 3, 6, 5, 4],
        )

    def test_single_row_and_column(self):
        self.assertEqual(self.solution.spiralOrder([[1, 2, 3]]), [1, 2, 3])
        self.assertEqual(self.solution.spiralOrder([[1], [2], [3]]), [1, 2, 3])
        self.assertEqual(self.solution.spiralOrder([[42]]), [42])


if __name__ == "__main__":
    unittest.main()
