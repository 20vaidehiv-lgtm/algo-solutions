import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice102 import letter_percentage  # noqa: E402


class LetterPercentageTest(unittest.TestCase):
    def test_examples_and_case_insensitivity(self):
        self.assertEqual(letter_percentage("foobar", "o"), 33)
        self.assertEqual(letter_percentage("hello", "l"), 40)
        self.assertEqual(letter_percentage("Hello", "H"), 20)
        self.assertEqual(letter_percentage("aaaa", "A"), 100)

    def test_missing_and_empty(self):
        self.assertEqual(letter_percentage("abc", "z"), 0)
        self.assertEqual(letter_percentage("", "a"), 0)


if __name__ == "__main__":
    unittest.main()
