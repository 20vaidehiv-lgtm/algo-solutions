import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice158 import Solution  # noqa: E402


class ContainsDuplicateTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertTrue(sol.hasDuplicate([1, 2, 3, 1]))
        self.assertFalse(sol.hasDuplicate([1, 2, 3, 4]))


if __name__ == "__main__":
    unittest.main()

