import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice50 import longestCommonPrefix  # noqa: E402


class LongestCommonPrefixTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(longestCommonPrefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(longestCommonPrefix(["dog", "racecar", "car"]), "")
        self.assertEqual(longestCommonPrefix([""]), "")


if __name__ == "__main__":
    unittest.main()

