import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice277 import Solution  # noqa: E402


class CheckIfPangramTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertTrue(sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
        self.assertFalse(sol.checkIfPangram("leetcode"))


if __name__ == "__main__":
    unittest.main()

