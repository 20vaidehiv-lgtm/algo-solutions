import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice84 import solveNQueens  # noqa: E402


class NQueensTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(len(solveNQueens(4)), 2)
        self.assertEqual(solveNQueens(1), [["Q"]])
        self.assertEqual(solveNQueens(2), [])


if __name__ == "__main__":
    unittest.main()

