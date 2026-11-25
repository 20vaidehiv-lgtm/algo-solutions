import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice356 import minimumDistances  # noqa: E402


class MinimumDistancesTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(minimumDistances([7, 1, 3, 4, 1, 7]), 3)
        self.assertEqual(minimumDistances([1, 2, 3, 4, 5]), -1)
        self.assertEqual(minimumDistances([1, 1]), 1)

    def test_empty(self):
        self.assertEqual(minimumDistances([]), -1)


if __name__ == "__main__":
    unittest.main()
