import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice124 import twoSum  # noqa: E402


class TwoSumTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(twoSum([1, 2, 3, 5], 7), [1, 3])
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(twoSum([1, 2, 3], 10), [])


if __name__ == "__main__":
    unittest.main()

