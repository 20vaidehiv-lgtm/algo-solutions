import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice10 import first_letter_twice  # noqa: E402


class FirstLetterTwiceTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(first_letter_twice("abccbaacz"), "c")
        self.assertEqual(first_letter_twice("abcdd"), "d")
        self.assertEqual(first_letter_twice("hello"), "l")

    def test_edge_cases(self):
        self.assertIsNone(first_letter_twice("abcdefghijklmnopqrstuvwxyz"))
        self.assertIsNone(first_letter_twice("a"))
        self.assertIsNone(first_letter_twice(""))
        self.assertEqual(first_letter_twice("aa"), "a")


if __name__ == "__main__":
    unittest.main()
