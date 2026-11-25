import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice412 import Solution  # noqa: E402


class MaxAreaTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(sol.maxArea([1, 1]), 1)
        self.assertEqual(sol.maxArea([4, 3, 2, 1, 4]), 16)
        self.assertEqual(sol.maxArea([1, 2, 1]), 2)


if __name__ == "__main__":
    unittest.main()

