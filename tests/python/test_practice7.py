import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice7 import merge  # noqa: E402


class MergeIntervalsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
        self.assertEqual(merge([[1, 4], [4, 5]]), [[1, 5]])

    def test_edge_cases(self):
        self.assertEqual(merge([]), [])
        self.assertEqual(merge([[1, 4]]), [[1, 4]])
        self.assertEqual(merge([[1, 4], [2, 3]]), [[1, 4]])
        self.assertEqual(merge([[5, 6], [1, 4]]), [[1, 4], [5, 6]])


if __name__ == "__main__":
    unittest.main()
