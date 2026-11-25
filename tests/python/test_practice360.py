import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice360 import alternatingCharacters  # noqa: E402


class AlternatingCharactersTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("BBBBB"), 4)
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
        self.assertEqual(alternatingCharacters("AAABBB"), 4)

    def test_empty_and_single(self):
        self.assertEqual(alternatingCharacters(""), 0)
        self.assertEqual(alternatingCharacters("A"), 0)


if __name__ == "__main__":
    unittest.main()
