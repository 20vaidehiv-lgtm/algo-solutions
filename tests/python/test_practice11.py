import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice11 import generateMatrix  # noqa: E402


class GenerateMatrixTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(generateMatrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
        self.assertEqual(generateMatrix(1), [[1]])
        self.assertEqual(generateMatrix(2), [[1, 2], [4, 3]])
        self.assertEqual(
            generateMatrix(4),
            [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]],
        )

    def test_edge_cases(self):
        self.assertEqual(generateMatrix(0), [])


if __name__ == "__main__":
    unittest.main()
