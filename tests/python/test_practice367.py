import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice367 import Solution  # noqa: E402


class MinimumAbsDifferenceTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(
            self.sol.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]),
            [[-14, -10], [19, 23], [23, 27]],
        )
        self.assertEqual(
            self.sol.minimumAbsDifference([-25, -51, -29, -23, 57, -18]),
            [[-25, -23]],
        )
        self.assertEqual(self.sol.minimumAbsDifference([1, 3, 6, 10, 15]), [[1, 3]])

    def test_all_consecutive(self):
        self.assertEqual(self.sol.minimumAbsDifference([4, 2, 1, 3]), [[1, 2], [2, 3], [3, 4]])


if __name__ == "__main__":
    unittest.main()
