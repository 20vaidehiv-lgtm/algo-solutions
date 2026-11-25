import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice53 import two_sum  # noqa: E402


class TwoSumTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum([], 5), [])


if __name__ == "__main__":
    unittest.main()

