import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice31 import generate_palindrome_ascii  # noqa: E402


class GeneratePalindromeAsciiTest(unittest.TestCase):
    def test_generated_binary_is_palindrome(self):
        s, binary_len = generate_palindrome_ascii()
        bits = "".join(format(ord(c), "07b") for c in s)
        self.assertEqual(len(bits), binary_len)
        self.assertGreater(binary_len, 100)
        self.assertEqual(bits, bits[::-1])


if __name__ == "__main__":
    unittest.main()

