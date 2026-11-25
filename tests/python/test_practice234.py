import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice234 import Solution  # noqa: E402


class CommonCharsTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(sorted(self.solution.commonChars(["bella", "label", "roller"])), ["e", "l", "l"])
        self.assertEqual(sorted(self.solution.commonChars(["cool", "lock", "cook"])), ["c", "o"])
        self.assertEqual(self.solution.commonChars(["abc", "bcd", "cde"]), ["c"])

    def test_no_common_chars(self):
        self.assertEqual(self.solution.commonChars(["abc", "def"]), [])


if __name__ == "__main__":
    unittest.main()
