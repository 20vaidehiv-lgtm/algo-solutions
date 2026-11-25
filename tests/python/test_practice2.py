import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice2 import maxSubArray  # noqa: E402


class MaxSubArrayTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(maxSubArray([1]), 1)
        self.assertEqual(maxSubArray([5, 4, -1, 7, 8]), 23)

    def test_edge_cases(self):
        self.assertEqual(maxSubArray([]), 0)
        self.assertEqual(maxSubArray([-1, -2, -3, -4]), -1)
        self.assertEqual(maxSubArray([-3, 0, -2]), 0)
        self.assertEqual(maxSubArray([5, -10, 6]), 6)


if __name__ == "__main__":
    unittest.main()
