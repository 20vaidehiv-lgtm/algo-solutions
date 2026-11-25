import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice428 import decode  # noqa: E402


class DecodeWaysTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(decode("12"), 2)
        self.assertEqual(decode("226"), 3)

    def test_zeroes(self):
        self.assertEqual(decode("06"), 0)
        self.assertEqual(decode("0"), 0)


if __name__ == "__main__":
    unittest.main()

