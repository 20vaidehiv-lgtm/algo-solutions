import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice4 import countCapitalLetters  # noqa: E402


class CountCapitalLettersTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(countCapitalLetters("HelloWorld"), 3)
        self.assertEqual(countCapitalLetters("hello"), 1)
        self.assertEqual(countCapitalLetters("HELLO"), 6)
        self.assertEqual(countCapitalLetters("hElLo"), 3)

    def test_edge_cases(self):
        self.assertEqual(countCapitalLetters(""), 1)
        self.assertEqual(countCapitalLetters("123!@#"), 1)
        self.assertEqual(countCapitalLetters("A"), 2)


if __name__ == "__main__":
    unittest.main()
