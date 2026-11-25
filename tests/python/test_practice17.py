import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice17 import isPalindrome1, isPalindrome2  # noqa: E402


class PalindromeNumberTest(unittest.TestCase):
    def test_palindromes(self):
        for value in (0, 1, 121, 1001, 12321):
            self.assertTrue(isPalindrome1(value))
            self.assertTrue(isPalindrome2(value))

    def test_non_palindromes(self):
        for value in (-121, 10, 123):
            self.assertFalse(isPalindrome1(value))
            self.assertFalse(isPalindrome2(value))


if __name__ == "__main__":
    unittest.main()
