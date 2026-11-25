import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice263 import subarraySum  # noqa: E402


class SubarraySumTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(subarraySum([1, 2, 3, 7, 5], 12), [2, 4])
        self.assertEqual(subarraySum([1, 2, 3], 100), [-1])


if __name__ == "__main__":
    unittest.main()

