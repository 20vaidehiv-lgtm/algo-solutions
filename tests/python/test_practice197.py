import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice197 import validBraces, valid_braces  # noqa: E402


class ValidBracesTest(unittest.TestCase):
    def test_valid_and_invalid(self):
        for fn in (valid_braces, validBraces):
            self.assertTrue(fn("()"))
            self.assertTrue(fn("(){}[]"))
            self.assertTrue(fn("([{}])"))
            self.assertFalse(fn("(}"))
            self.assertFalse(fn("[(])"))
            self.assertFalse(fn("[({})](]"))


if __name__ == "__main__":
    unittest.main()
