import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice26 import Solution  # noqa: E402


class IntToRomanTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.intToRoman(3), "III")
        self.assertEqual(sol.intToRoman(4), "IV")
        self.assertEqual(sol.intToRoman(9), "IX")
        self.assertEqual(sol.intToRoman(58), "LVIII")
        self.assertEqual(sol.intToRoman(1994), "MCMXCIV")
        self.assertEqual(sol.intToRoman(3999), "MMMCMXCIX")


if __name__ == "__main__":
    unittest.main()

