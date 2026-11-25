import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice385 import number_of_pairs  # noqa: E402


class NumberOfPairsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(number_of_pairs(["red", "red", "red", "red", "red", "red"]), 3)
        self.assertEqual(number_of_pairs(["red", "green", "red", "blue", "blue"]), 2)
        self.assertEqual(number_of_pairs(["red", "green", "blue"]), 0)

    def test_empty(self):
        self.assertEqual(number_of_pairs([]), 0)


if __name__ == "__main__":
    unittest.main()
