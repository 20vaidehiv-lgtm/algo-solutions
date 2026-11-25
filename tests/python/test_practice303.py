import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice303 import Solution  # noqa: E402


class MinimumAverageTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]), 5.5)
        self.assertEqual(self.sol.minimumAverage([1, 9, 8, 3, 10, 5]), 5.5)
        self.assertEqual(self.sol.minimumAverage([1, 2, 3, 7, 8, 9]), 5.0)

    def test_pair(self):
        self.assertEqual(self.sol.minimumAverage([1, 3]), 2.0)


if __name__ == "__main__":
    unittest.main()
