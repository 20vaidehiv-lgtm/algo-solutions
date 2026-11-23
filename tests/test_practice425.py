import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "solutions", "python"))

from practice425 import min_window  # noqa: E402


class MinWindowSubstringTest(unittest.TestCase):
    def test_single_character_window(self):
        self.assertEqual(min_window("a", "a"), "a")

    def test_window_shrinks_past_matched_characters(self):
        self.assertEqual(min_window("aab", "ab"), "ab")
        self.assertEqual(min_window("ADOBECODEBANC", "ABC"), "BANC")


if __name__ == "__main__":
    unittest.main()
