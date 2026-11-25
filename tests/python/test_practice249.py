import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice249 import palindrome  # noqa: E402


class ValidPalindromeTest(unittest.TestCase):
    def test_palindromes(self):
        self.assertTrue(palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(palindrome("race a car"))
        self.assertTrue(palindrome(" "))
        self.assertTrue(palindrome("0P0"))


if __name__ == "__main__":
    unittest.main()
