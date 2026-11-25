import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice194 import sort_by_binary_ones  # noqa: E402


class SortByBinaryOnesTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sort_by_binary_ones([1, 15, 5, 7, 3]), [15, 7, 5, 3, 1])
        self.assertEqual(sort_by_binary_ones([5, 2049, 3]), [3, 5, 2049])
        self.assertEqual(
            sort_by_binary_ones([99, 51, 21, 7, 44, 50, 49, 25, 5, 80, 33, 1]),
            [51, 99, 7, 21, 25, 44, 49, 50, 5, 33, 80, 1],
        )


if __name__ == "__main__":
    unittest.main()
