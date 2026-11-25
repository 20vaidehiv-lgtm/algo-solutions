# Note: solutions/python/practice422.py is currently marked IN PROGRESS.
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice422 import convert  # noqa: E402


class ZigzagConversionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")

    def test_single_row(self):
        self.assertEqual(convert("A", 1), "A")


if __name__ == "__main__":
    unittest.main()

