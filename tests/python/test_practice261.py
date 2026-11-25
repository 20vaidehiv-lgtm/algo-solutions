import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice261 import Solution  # noqa: E402


class DiagonalSumTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 25)
        self.assertEqual(sol.diagonalSum([[5]]), 5)


if __name__ == "__main__":
    unittest.main()

