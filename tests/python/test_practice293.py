import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice293 import Solution  # noqa: E402


class GetMinDistanceTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.getMinDistance([1, 2, 3, 4, 5], 5, 3), 1)
        self.assertEqual(sol.getMinDistance([1], 1, 0), 0)
        self.assertEqual(sol.getMinDistance([5, 3, 6], 5, 2), 2)


if __name__ == "__main__":
    unittest.main()

