import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice248 import sums  # noqa: E402


class TwoSumTest(unittest.TestCase):
    def test_found_and_not_found(self):
        self.assertEqual(sums([1, 2, 3, 4], 7), (2, 3))
        self.assertEqual(sums([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(sums([1, 2, 3], 7), -1)


if __name__ == "__main__":
    unittest.main()
