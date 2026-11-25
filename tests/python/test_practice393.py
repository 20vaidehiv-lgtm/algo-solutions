import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice393 import is_solved  # noqa: E402


class TicTacToeCheckerTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(is_solved([[0, 0, 2], [0, 0, 0], [1, 0, 1]]), -1)
        self.assertEqual(is_solved([[0, 0, 1], [0, 1, 0], [1, 0, 0]]), 1)
        self.assertEqual(is_solved([[1, 2, 1], [2, 1, 2], [2, 1, 2]]), 0)

    def test_row_col_diag_wins(self):
        self.assertEqual(is_solved([[2, 2, 2], [0, 1, 1], [1, 0, 0]]), 2)
        self.assertEqual(is_solved([[1, 2, 0], [1, 2, 0], [0, 2, 1]]), 2)
        self.assertEqual(is_solved([[1, 2, 0], [0, 1, 2], [0, 0, 1]]), 1)


if __name__ == "__main__":
    unittest.main()
