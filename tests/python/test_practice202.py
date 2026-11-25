import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice202 import countingValleys  # noqa: E402


class CountingValleysTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(countingValleys(8, "UDDDUDUU"), 1)
        self.assertEqual(countingValleys(12, "DDUUDDUDUUUD"), 2)

    def test_no_valleys(self):
        self.assertEqual(countingValleys(4, "UUDD"), 0)


if __name__ == "__main__":
    unittest.main()
