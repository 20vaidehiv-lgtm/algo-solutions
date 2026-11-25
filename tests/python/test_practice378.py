import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice378 import Solution  # noqa: E402


class FindPivotIndexTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.pivotIndex([1, 7, 3, 6, 5, 6]), 3)
        self.assertEqual(self.sol.pivotIndex([2, 1, -1]), 0)
        self.assertEqual(self.sol.pivotIndex([1, 2, 3]), -1)

    def test_right_edge_and_empty(self):
        self.assertEqual(self.sol.pivotIndex([-1, 1, 5]), 2)
        self.assertEqual(self.sol.pivotIndex([]), -1)


if __name__ == "__main__":
    unittest.main()
