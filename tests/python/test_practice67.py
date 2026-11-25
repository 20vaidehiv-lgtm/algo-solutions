import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice67 import filter_strings_by_substring  # noqa: E402


class FilterStringsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(filter_strings_by_substring(["hello", "world", "hello world"], "lo"), "hello\nhello world")
        self.assertEqual(filter_strings_by_substring(["abc", "def"], "x"), "")


if __name__ == "__main__":
    unittest.main()

