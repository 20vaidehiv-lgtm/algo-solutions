import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice1 import totalNQueens  # noqa: E402


class TotalNQueensTest(unittest.TestCase):
    def test_standard_boards(self):
        self.assertEqual(totalNQueens(4), 2)
        self.assertEqual(totalNQueens(5), 10)
        self.assertEqual(totalNQueens(6), 4)

    def test_small_boards(self):
        self.assertEqual(totalNQueens(1), 1)
        self.assertEqual(totalNQueens(2), 0)
        self.assertEqual(totalNQueens(3), 0)


if __name__ == "__main__":
    unittest.main()
