import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice424 import letter_combinations  # noqa: E402


class LetterCombinationsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            letter_combinations("23"),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        )
        self.assertEqual(letter_combinations("2"), ["a", "b", "c"])

    def test_empty(self):
        self.assertEqual(letter_combinations(""), [])


if __name__ == "__main__":
    unittest.main()

