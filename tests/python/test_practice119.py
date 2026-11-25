import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice119 import sort_characters_by_frequency  # noqa: E402


class SortCharsByFreqTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sort_characters_by_frequency("aabbccc"), "cccaabb")
        self.assertEqual(sort_characters_by_frequency("hello"), "lleho")
        self.assertEqual(sort_characters_by_frequency(""), "")


if __name__ == "__main__":
    unittest.main()

