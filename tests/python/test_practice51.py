import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice51 import equalDivisiblePairs  # noqa: E402


class EqualDivisiblePairsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(equalDivisiblePairs([3, 1, 2, 2, 2, 1, 3], 2), 4)
        self.assertEqual(equalDivisiblePairs([1, 2, 3, 4], 1), 0)
        self.assertEqual(equalDivisiblePairs([], 1), 0)


if __name__ == "__main__":
    unittest.main()

