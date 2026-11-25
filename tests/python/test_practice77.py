import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice77 import is_valid  # noqa: E402


class TimeLimitValidatorTest(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(is_valid("02:30:00", ["00:45:00", "01:00:00", "00:30:00"]))
        self.assertFalse(is_valid("02:30:00", ["01:45:00", "01:00:00", "00:30:00"]))
        self.assertTrue(is_valid("01:00:00", []))


if __name__ == "__main__":
    unittest.main()

