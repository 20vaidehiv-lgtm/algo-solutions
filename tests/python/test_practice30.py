import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice30 import sumAlternatingDigit  # noqa: E402


class AlternatingDigitSumTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sumAlternatingDigit(4567), -2)
        self.assertEqual(sumAlternatingDigit(123), 2)
        self.assertEqual(sumAlternatingDigit(10), 1)
        self.assertEqual(sumAlternatingDigit(0), 0)


if __name__ == "__main__":
    unittest.main()

