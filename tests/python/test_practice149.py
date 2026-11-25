import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice149 import Solution  # noqa: E402


class CountPairsTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.countPairs([-1, 1, 2, 3, 1], 2), 3)
        self.assertEqual(sol.countPairs([-6, 2, 5, -2, -7, -1, 3], -2), 10)


if __name__ == "__main__":
    unittest.main()

