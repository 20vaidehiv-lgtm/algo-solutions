import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice361 import Solution  # noqa: E402


class NumberOfIslandsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        grid1 = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        self.assertEqual(self.sol.numIslands(grid1), 1)

        grid2 = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        self.assertEqual(self.sol.numIslands(grid2), 3)

        grid3 = [
            ["1", "1", "1"],
            ["0", "1", "0"],
            ["1", "1", "1"],
        ]
        self.assertEqual(self.sol.numIslands(grid3), 1)

    def test_all_water(self):
        self.assertEqual(self.sol.numIslands([["0", "0"], ["0", "0"]]), 0)


if __name__ == "__main__":
    unittest.main()
