import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice151 import Solution  # noqa: E402


class LargestLocalTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
        self.assertEqual(sol.largestLocal(grid), [[9, 9], [8, 6]])


if __name__ == "__main__":
    unittest.main()

