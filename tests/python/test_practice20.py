import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice20 import isDecimal, isInteger, isNumber  # noqa: E402


class ValidNumberTest(unittest.TestCase):
    def test_valid_numbers(self):
        for s in ("2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93"):
            self.assertTrue(isNumber(s), f"Expected {s!r} to be valid")

    def test_invalid_numbers(self):
        for s in ("abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "", "."):
            self.assertFalse(isNumber(s), f"Expected {s!r} to be invalid")

    def test_helpers(self):
        self.assertTrue(isDecimal("-0.5"))
        self.assertFalse(isDecimal("."))
        self.assertTrue(isInteger("+42"))
        self.assertFalse(isInteger("3.14"))


if __name__ == "__main__":
    unittest.main()
