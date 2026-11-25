import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice352 import Solution  # noqa: E402


class RowWithMax1sTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.rowWithMax1s([[0, 1, 1], [0, 0, 1], [1, 1, 1]]), 2)
        self.assertEqual(self.sol.rowWithMax1s([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), -1)
        self.assertEqual(self.sol.rowWithMax1s([[1, 1, 1], [0, 0, 0], [0, 0, 0]]), 0)

    def test_tie_returns_first_row(self):
        self.assertEqual(self.sol.rowWithMax1s([[0, 1], [1, 0]]), 0)


if __name__ == "__main__":
    unittest.main()
