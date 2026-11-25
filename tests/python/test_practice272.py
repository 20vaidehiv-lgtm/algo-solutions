import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice272 import Solution  # noqa: E402


class DistributeCandiesTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.distributeCandies([1, 1, 2, 2, 3, 3]), 3)
        self.assertEqual(sol.distributeCandies([1, 1, 2, 3]), 2)
        self.assertEqual(sol.distributeCandies([6, 6, 6, 6]), 1)


if __name__ == "__main__":
    unittest.main()

