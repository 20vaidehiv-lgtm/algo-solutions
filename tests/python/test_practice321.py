import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice321 import Solution  # noqa: E402


class SplitArrayTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertTrue(self.sol.isPossibleToSplit([1, 1, 2, 2, 3, 4]))
        self.assertFalse(self.sol.isPossibleToSplit([1, 1, 2, 2, 2, 2, 3, 4]))

    def test_edge_cases(self):
        self.assertFalse(self.sol.isPossibleToSplit([1, 1, 1, 2]))
        self.assertTrue(self.sol.isPossibleToSplit([1, 2, 3, 4]))


if __name__ == "__main__":
    unittest.main()
