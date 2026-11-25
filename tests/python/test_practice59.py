import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice59 import buddy_strings  # noqa: E402


class BuddyStringsTest(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(buddy_strings("ab", "ba"))
        self.assertTrue(buddy_strings("aa", "aa"))
        self.assertFalse(buddy_strings("abc", "abd"))


if __name__ == "__main__":
    unittest.main()

