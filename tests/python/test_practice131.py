import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice131 import spiral_matrix_list  # noqa: E402


class SpiralMatrixTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            spiral_matrix_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        )
        self.assertEqual(
            spiral_matrix_list([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        )

    def test_single_row(self):
        self.assertEqual(spiral_matrix_list([[1, 2, 3]]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
