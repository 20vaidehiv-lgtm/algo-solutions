import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice291 import appendAndDelete  # noqa: E402


class AppendAndDeleteTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(appendAndDelete("hackerhappy", "hackerrank", 9), "Yes")
        self.assertEqual(appendAndDelete("ashley", "ash", 2), "No")
        self.assertEqual(appendAndDelete("ash", "ashley", 1), "No")


if __name__ == "__main__":
    unittest.main()

