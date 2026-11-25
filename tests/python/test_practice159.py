import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice159 import Solution  # noqa: E402


class RestoreStringTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]), "leetcode")
        self.assertEqual(sol.restoreString("abc", [0, 1, 2]), "abc")


if __name__ == "__main__":
    unittest.main()

