import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice283 import repeatedString  # noqa: E402


class RepeatedStringTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(repeatedString("a", 1000000000000), 1000000000000)
        self.assertEqual(repeatedString("aba", 10), 7)
        self.assertEqual(repeatedString("abcac", 10), 4)


if __name__ == "__main__":
    unittest.main()

