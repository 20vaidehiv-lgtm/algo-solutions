import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice19 import minPathSum  # noqa: E402


class MinPathSumTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)
        self.assertEqual(minPathSum([[1, 2, 3], [4, 5, 6]]), 12)

    def test_edge_cases(self):
        self.assertEqual(minPathSum([[1]]), 1)
        self.assertEqual(minPathSum([[1, 2], [3, 4]]), 7)
        self.assertEqual(minPathSum([]), 0)


if __name__ == "__main__":
    unittest.main()
