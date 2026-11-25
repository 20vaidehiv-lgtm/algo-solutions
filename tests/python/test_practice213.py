import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice213 import decrypt, encrypt  # noqa: E402


class AlternatingSplitTest(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(encrypt("This is a test!", 1), "hsi  etTi sats!")
        self.assertEqual(encrypt("This is a test!", 2), "s eT ashi tist!")
        self.assertEqual(encrypt("", 3), "")

    def test_decrypt(self):
        self.assertEqual(decrypt("This is a test!", 0), "This is a test!")
        self.assertEqual(decrypt("hsi  etTi sats!", 1), "This is a test!")
        self.assertEqual(decrypt("s eT ashi tist!", 2), "This is a test!")
        self.assertEqual(decrypt("This is a test!", -1), "This is a test!")


if __name__ == "__main__":
    unittest.main()
