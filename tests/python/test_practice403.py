import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice403 import sum_pairs  # noqa: E402


class SumPairsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_pairs([10, 5, 2, 3, 7, 5], 10), [3, 7])
        self.assertEqual(sum_pairs([1, -2, 3, 0, -6, 1], -6), [0, -6])
        self.assertEqual(sum_pairs([5, 5], 10), [5, 5])
        self.assertIsNone(sum_pairs([5], 10))
        self.assertIsNone(sum_pairs([], 0))


if __name__ == "__main__":
    unittest.main()

