import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice168 import vowel_recognition  # noqa: E402


class VowelRecognitionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(vowel_recognition("aba"), 6)
        self.assertEqual(vowel_recognition("abc"), 3)
        self.assertEqual(vowel_recognition("baceb"), 16)


if __name__ == "__main__":
    unittest.main()

