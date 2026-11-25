import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice8 import insert  # noqa: E402


class InsertIntervalTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
        self.assertEqual(
            insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
            [[1, 2], [3, 10], [12, 16]],
        )

    def test_edge_cases(self):
        self.assertEqual(insert([], [5, 7]), [[5, 7]])
        self.assertEqual(insert([[1, 5]], [2, 3]), [[1, 5]])
        self.assertEqual(insert([[1, 5]], [6, 8]), [[1, 5], [6, 8]])
        self.assertEqual(insert([[1, 5]], [0, 0]), [[0, 0], [1, 5]])


if __name__ == "__main__":
    unittest.main()
