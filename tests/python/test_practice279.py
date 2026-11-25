import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice279 import is_leap  # noqa: E402


class LeapYearTest(unittest.TestCase):
    def test_examples(self):
        self.assertFalse(is_leap(1990))
        self.assertTrue(is_leap(2000))
        self.assertFalse(is_leap(1900))
        self.assertTrue(is_leap(2024))


if __name__ == "__main__":
    unittest.main()

