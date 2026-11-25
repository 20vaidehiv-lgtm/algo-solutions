import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice302 import lis  # noqa: E402


class LongestIncreasingSubsequenceTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(lis([3, 1, 8, 2, 5]), 3)
        self.assertEqual(lis([5, 2, 8, 6, 3, 6, 9, 5]), 4)

    def test_monotonic(self):
        self.assertEqual(lis([1, 2, 3, 4]), 4)
        self.assertEqual(lis([5, 4, 3, 2, 1]), 1)


if __name__ == "__main__":
    unittest.main()
