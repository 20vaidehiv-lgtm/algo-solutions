import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice128 import get_length  # noqa: E402


class LengthOfLastWordTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(get_length("Hello World"), 5)
        self.assertEqual(get_length("     fly me   to    the    mooon   "), 5)

    def test_single_word(self):
        self.assertEqual(get_length("luffy"), 5)


if __name__ == "__main__":
    unittest.main()
