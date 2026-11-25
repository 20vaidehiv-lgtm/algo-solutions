import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice48 import unscramble_string  # noqa: E402


class UnscrambleStringTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(unscramble_string("H!e ldllor ow"), "Hello world!")
        self.assertEqual(unscramble_string("abcde"), "acebd")
        self.assertEqual(unscramble_string("a"), "a")


if __name__ == "__main__":
    unittest.main()

