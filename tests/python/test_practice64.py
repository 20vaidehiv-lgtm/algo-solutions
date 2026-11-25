import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice64 import longest_substring_without_repeating  # noqa: E402


class LongestSubstringTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_substring_without_repeating("abcabcbb"), 3)
        self.assertEqual(longest_substring_without_repeating("bbbbb"), 1)
        self.assertEqual(longest_substring_without_repeating("pwwkew"), 3)
        self.assertEqual(longest_substring_without_repeating(""), 0)


if __name__ == "__main__":
    unittest.main()

