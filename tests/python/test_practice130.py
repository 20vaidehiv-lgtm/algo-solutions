import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice130 import merge_intervals  # noqa: E402


class MergeIntervalsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]],
        )
        self.assertEqual(merge_intervals([[1, 4], [4, 5]]), [[1, 5]])

    def test_unsorted_intervals(self):
        self.assertEqual(merge_intervals([[1, 4], [0, 4]]), [[0, 4]])


if __name__ == "__main__":
    unittest.main()
