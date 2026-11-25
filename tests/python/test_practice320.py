import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice320 import Solution  # noqa: E402


class TrimTrailingVowelsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.trimTrailingVowels("a"), "")
        self.assertEqual(self.sol.trimTrailingVowels("ba"), "b")
        self.assertEqual(self.sol.trimTrailingVowels("idea"), "id")

    def test_no_trailing_vowels_and_all_vowels(self):
        self.assertEqual(self.sol.trimTrailingVowels("aeiou"), "")
        self.assertEqual(self.sol.trimTrailingVowels("xyz"), "xyz")


if __name__ == "__main__":
    unittest.main()
