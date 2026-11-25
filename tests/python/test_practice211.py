import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice211 import is_valid_IP  # noqa: E402


class IpValidationTest(unittest.TestCase):
    def test_valid_ips(self):
        self.assertTrue(is_valid_IP("123.123.123.123"))
        self.assertTrue(is_valid_IP("1.2.3.4"))
        self.assertTrue(is_valid_IP("0.0.0.0"))
        self.assertTrue(is_valid_IP("255.255.255.255"))

    def test_invalid_ips(self):
        self.assertFalse(is_valid_IP("123.123.123.1234"))
        self.assertFalse(is_valid_IP("123.123.123"))
        self.assertFalse(is_valid_IP("1.2.3"))
        self.assertFalse(is_valid_IP("01.02.03.04"))
        self.assertFalse(is_valid_IP("256.1.2.3"))
        self.assertFalse(is_valid_IP("1.2.3.a"))
        self.assertFalse(is_valid_IP(""))


if __name__ == "__main__":
    unittest.main()
