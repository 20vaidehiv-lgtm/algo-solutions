import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice33 import Solution  # noqa: E402


class StrictlyPalindromicTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertFalse(sol.isStrictlyPalindromic(9))
        self.assertFalse(sol.isStrictlyPalindromic(4))


if __name__ == "__main__":
    unittest.main()

