import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice384 import countingSort  # noqa: E402


class CountingSortTest(unittest.TestCase):
    def test_examples(self):
        result = countingSort([1, 1, 3, 2, 1])
        self.assertEqual(len(result), 101)
        self.assertEqual(result[:5], [0, 3, 1, 1, 0])

    def test_sample_from_file(self):
        arr = [
            63, 54, 17, 78, 43, 70, 32, 97, 16, 94, 74, 18, 60, 61, 35, 83, 13, 56, 75, 52, 70, 12,
            24, 37, 17, 0, 16, 64, 34, 81, 82, 24, 69, 2, 30, 61, 83, 37, 97, 16, 70, 53, 0, 61, 12,
            17, 97, 67, 33, 30, 49, 70, 11, 40, 67, 94, 84, 60, 35, 58, 19, 81, 16, 14, 68, 46, 42,
            81, 75, 87, 13, 84, 33, 34, 14, 96, 7, 59, 17, 98, 79, 47, 71, 75, 8, 27, 73, 66, 64,
            12, 29, 35, 80, 78, 80, 6, 5, 24, 49, 82,
        ]
        result = countingSort(arr)
        self.assertEqual(sum(result), len(arr))
        self.assertEqual(result[0], 2)
        self.assertEqual(result[16], 4)
        self.assertEqual(result[100], 0)

    def test_empty(self):
        self.assertEqual(countingSort([]), [0] * 101)


if __name__ == "__main__":
    unittest.main()
