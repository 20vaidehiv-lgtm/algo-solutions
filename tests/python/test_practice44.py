import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice44 import Solution  # noqa: E402


class WordPatternTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertTrue(sol.wordPattern("abba", "dog cat cat dog"))
        self.assertFalse(sol.wordPattern("abba", "dog cat cat fish"))
        self.assertFalse(sol.wordPattern("jquery", "jquery"))


if __name__ == "__main__":
    unittest.main()

