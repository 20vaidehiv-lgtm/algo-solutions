import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice15 import uniquePaths  # noqa: E402


class UniquePathsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(uniquePaths(3, 7), 28)
        self.assertEqual(uniquePaths(3, 2), 3)
        self.assertEqual(uniquePaths(7, 3), 28)

    def test_edge_cases(self):
        self.assertEqual(uniquePaths(1, 1), 1)
        self.assertEqual(uniquePaths(1, 10), 1)
        self.assertEqual(uniquePaths(10, 1), 1)
        self.assertEqual(uniquePaths(2, 2), 2)


if __name__ == "__main__":
    unittest.main()
