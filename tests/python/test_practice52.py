import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice52 import find_max_area_longest_diagonal  # noqa: E402


class MaxAreaLongestDiagonalTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(find_max_area_longest_diagonal([(3, 4), (5, 12), (6, 8)]), 60)
        self.assertEqual(find_max_area_longest_diagonal([(4, 3), (8, 6)]), 48)
        self.assertEqual(find_max_area_longest_diagonal([]), 0)


if __name__ == "__main__":
    unittest.main()

