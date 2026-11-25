import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice72 import clearDigits  # noqa: E402


class ClearDigitsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(clearDigits("a1bc2d3"), "b")
        self.assertEqual(clearDigits("abc123"), "")
        self.assertEqual(clearDigits("abc"), "abc")


if __name__ == "__main__":
    unittest.main()

