import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice243 import format_duration  # noqa: E402


class FormatDurationTest(unittest.TestCase):
    def test_examples_and_edge_cases(self):
        self.assertEqual(format_duration(0), "now")
        self.assertEqual(format_duration(1), "1 second")
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")
        self.assertEqual(format_duration(3600), "1 hour")
        self.assertEqual(format_duration(3660), "1 hour and 1 minute")
        self.assertEqual(format_duration(31_556_926), "1 year, 5 hours, 48 minutes and 46 seconds")
        self.assertEqual(format_duration(132030240), "4 years, 68 days, 3 hours and 4 minutes")


if __name__ == "__main__":
    unittest.main()
