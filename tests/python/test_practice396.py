import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice396 import checkio  # noqa: E402


class CommonWordsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(checkio("one,two,three", "four,three,two,one"), "one,three,two")
        self.assertEqual(checkio("one,two,three", "four,five,six"), "")
        self.assertEqual(checkio("hello,world", "hello,earth"), "hello")

    def test_identical_strings(self):
        self.assertEqual(checkio("b,a,c", "c,b,a"), "a,b,c")


if __name__ == "__main__":
    unittest.main()
