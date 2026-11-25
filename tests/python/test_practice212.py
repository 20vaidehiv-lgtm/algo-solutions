import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice212 import sum_dig_pow  # noqa: E402


class SumDigPowTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
        self.assertEqual(sum_dig_pow(90, 100), [])

    def test_larger_range_and_single(self):
        self.assertEqual(sum_dig_pow(10, 150), [89, 135])
        self.assertEqual(sum_dig_pow(89, 89), [89])


if __name__ == "__main__":
    unittest.main()
