import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice157 import Solution  # noqa: E402


class CountMaxOrSubsetsTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.countMaxOrSubsets([3, 1]), 2)
        self.assertEqual(sol.countMaxOrSubsets([2, 2, 2]), 7)
        self.assertEqual(sol.countMaxOrSubsets([3, 2, 1, 5]), 6)


if __name__ == "__main__":
    unittest.main()

