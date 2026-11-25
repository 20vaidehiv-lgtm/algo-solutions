import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice273 import Solution  # noqa: E402


class KeyboardRowTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.findWords(["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"])
        self.assertEqual(sol.findWords(["adsdf", "sfd"]), ["adsdf", "sfd"])


if __name__ == "__main__":
    unittest.main()

