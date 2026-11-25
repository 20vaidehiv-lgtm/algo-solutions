import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice173 import merge_the_tools  # noqa: E402


class MergeTheToolsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(merge_the_tools("AABCAAADA", 3), "AB\nCA\nAD")
        self.assertEqual(merge_the_tools("AAABBBCCC", 3), "A\nB\nC")

    def test_single_char_chunks(self):
        self.assertEqual(merge_the_tools("ABCD", 1), "A\nB\nC\nD")
        self.assertEqual(merge_the_tools("ABCA", 4), "ABC")


if __name__ == "__main__":
    unittest.main()
