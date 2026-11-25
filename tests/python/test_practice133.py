import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice133 import longest_substring  # noqa: E402


class LongestSubstringTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longest_substring("abcabcbb"), 3)
        self.assertEqual(longest_substring("bbbbb"), 1)
        self.assertEqual(longest_substring("pwwkew"), 3)
        self.assertEqual(longest_substring("abcdac"), 4)


if __name__ == "__main__":
    unittest.main()
