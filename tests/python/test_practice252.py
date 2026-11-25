import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice252 import substring  # noqa: E402


class LongestSubstringTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(substring("abcaba"), "abc")
        self.assertEqual(substring("abcdef"), "abcdef")
        self.assertEqual(substring(""), "")


if __name__ == "__main__":
    unittest.main()
