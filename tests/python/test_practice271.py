import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice271 import clean_string  # noqa: E402


class CleanStringTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(clean_string("abc#d##c"), "ac")
        self.assertEqual(clean_string("abc##d######"), "")
        self.assertEqual(clean_string(""), "")


if __name__ == "__main__":
    unittest.main()

