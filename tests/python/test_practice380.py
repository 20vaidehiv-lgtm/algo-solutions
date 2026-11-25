import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice380 import valid_phone_number  # noqa: E402


class ValidPhoneNumberTest(unittest.TestCase):
    def test_valid_numbers(self):
        self.assertTrue(valid_phone_number("(123) 456-7890"))
        self.assertTrue(valid_phone_number("(000) 000-0000"))

    def test_invalid_numbers(self):
        self.assertFalse(valid_phone_number("(123) 456-7890abc"))
        self.assertFalse(valid_phone_number("abc(123) 456-7890"))
        self.assertFalse(valid_phone_number("(1111)555 2345"))
        self.assertFalse(valid_phone_number("123-456-7890"))


if __name__ == "__main__":
    unittest.main()
