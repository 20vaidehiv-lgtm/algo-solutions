import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice417 import is_palindrome  # noqa: E402


class PalindromeNumberTest(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(0))
        self.assertFalse(is_palindrome(-121))
        self.assertFalse(is_palindrome(123))


if __name__ == "__main__":
    unittest.main()

