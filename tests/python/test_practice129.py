import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice129 import insert_interval  # noqa: E402


class InsertIntervalTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(insert_interval([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
        self.assertEqual(
            insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
            [[1, 2], [3, 10], [12, 16]],
        )

    def test_empty_intervals(self):
        self.assertEqual(insert_interval([], [5, 7]), [[5, 7]])


if __name__ == "__main__":
    unittest.main()
