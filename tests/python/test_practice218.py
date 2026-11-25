import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice218 import decode, encode  # noqa: E402


class VowelCodeTest(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode("hello"), "h2ll4")
        self.assertEqual(encode("h2ll4"), "h2ll4")
        self.assertEqual(encode("How are you today?"), "H4w 1r2 y45 t4d1y?")
        self.assertEqual(encode("aeiou"), "12345")

    def test_decode(self):
        self.assertEqual(decode("h2ll4"), "hello")
        self.assertEqual(decode("How are you today?"), "How are you today?")
        self.assertEqual(decode("H4w 1r2 y45 t4d1y?"), "How are you today?")
        self.assertEqual(decode("123456"), "aeiou6")


if __name__ == "__main__":
    unittest.main()
