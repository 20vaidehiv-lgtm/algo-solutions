import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice70 import most_frequent_even  # noqa: E402


class MostFrequentEvenTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(most_frequent_even([1, 2, 2, 3, 4, 4, 4, 5]), 4)
        self.assertIsNone(most_frequent_even([1, 3, 5]))
        self.assertEqual(most_frequent_even([2, 4, 6, 8]), 2)


if __name__ == "__main__":
    unittest.main()

