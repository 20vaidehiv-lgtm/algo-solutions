import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice43 import percentageString  # noqa: E402


class PercentageStringTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(percentageString("hello", "l"), 40)
        self.assertEqual(percentageString("aabbcc", "a"), 33)
        self.assertEqual(percentageString("", "a"), 0)


if __name__ == "__main__":
    unittest.main()

