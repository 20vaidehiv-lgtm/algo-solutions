import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice18 import uniquePathsWithObstacles  # noqa: E402


class UniquePathsWithObstaclesTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)
        self.assertEqual(uniquePathsWithObstacles([[0, 1], [0, 0]]), 1)

    def test_edge_cases(self):
        self.assertEqual(uniquePathsWithObstacles([[1]]), 0)
        self.assertEqual(uniquePathsWithObstacles([[0]]), 1)
        self.assertEqual(uniquePathsWithObstacles([[0, 0], [0, 0]]), 2)
        self.assertEqual(uniquePathsWithObstacles([]), 0)


if __name__ == "__main__":
    unittest.main()
