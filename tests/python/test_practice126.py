import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice126 import spiralMatrix  # noqa: E402


class SpiralMatrix2Test(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(spiralMatrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
        self.assertEqual(spiralMatrix(1), [[1]])


if __name__ == "__main__":
    unittest.main()

