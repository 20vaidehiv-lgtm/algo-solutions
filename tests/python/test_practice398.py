import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice398 import Solution  # noqa: E402


class IntToRomanTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(self.solution.intToRoman(1390), "MCCCXC")
        self.assertEqual(self.solution.intToRoman(79), "LXXIX")
        self.assertEqual(self.solution.intToRoman(3), "III")

    def test_subtractive_cases(self):
        self.assertEqual(self.solution.intToRoman(1994), "MCMXCIV")
        self.assertEqual(self.solution.intToRoman(58), "LVIII")


if __name__ == "__main__":
    unittest.main()
