import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice214 import solution  # noqa: E402


class RomanNumeralsDecoderTest(unittest.TestCase):
    def test_basic_and_subtractive(self):
        self.assertEqual(solution("XXI"), 21)
        self.assertEqual(solution("I"), 1)
        self.assertEqual(solution("IV"), 4)
        self.assertEqual(solution("MMVIII"), 2008)
        self.assertEqual(solution("MDCLIXIV"), 1663)
        self.assertEqual(solution("MCMXCIV"), 1994)

    def test_empty(self):
        self.assertEqual(solution(""), 0)


if __name__ == "__main__":
    unittest.main()
