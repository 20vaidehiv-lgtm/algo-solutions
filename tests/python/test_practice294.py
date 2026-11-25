# Note: solutions/python/practice294.py is currently incomplete (missing return statement).
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice294 import dayOfProgrammer  # noqa: E402


class DayOfProgrammerTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(dayOfProgrammer(2017), "13.09.2017")
        self.assertEqual(dayOfProgrammer(2016), "12.09.2016")
        self.assertEqual(dayOfProgrammer(1800), "12.09.1800")


if __name__ == "__main__":
    unittest.main()

