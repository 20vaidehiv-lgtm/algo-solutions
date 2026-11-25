import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice388 import strip_comments  # noqa: E402


class StripCommentsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]),
            "apples, pears\ngrapes\nbananas",
        )
        self.assertEqual(strip_comments("   a #b\nc\nd $e f g", ["#", "$"]), "   a\nc\nd")
        self.assertEqual(strip_comments("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")

    def test_no_markers(self):
        self.assertEqual(strip_comments("hello world", []), "hello world")


if __name__ == "__main__":
    unittest.main()
