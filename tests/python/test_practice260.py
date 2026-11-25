import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice260 import Solution  # noqa: E402


class CountKDifferenceTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.countKDifference([1, 2, 2, 1], 1), 4)
        self.assertEqual(sol.countKDifference([1, 3], 3), 0)
        self.assertEqual(sol.countKDifference([3, 2, 1, 5, 4], 2), 3)


if __name__ == "__main__":
    unittest.main()

