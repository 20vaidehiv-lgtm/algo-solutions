import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice431 import tribonacci  # noqa: E402


class TribonacciTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
        self.assertEqual(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])

    def test_short_n(self):
        self.assertEqual(tribonacci([1, 2, 3], 2), [1, 2])
        self.assertEqual(tribonacci([1, 2, 3], 0), [])


if __name__ == "__main__":
    unittest.main()

