import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice161 import Solution  # noqa: E402


class FindClosestTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.findClosest(1, 2, 3), 2)
        self.assertEqual(sol.findClosest(2, 7, 4), 1)
        self.assertEqual(sol.findClosest(1, 5, 3), 0)


if __name__ == "__main__":
    unittest.main()

