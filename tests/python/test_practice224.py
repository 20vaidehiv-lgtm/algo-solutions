import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice224 import Solution  # noqa: E402


class FourSumTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(
            self.solution.fourSum([1, 0, -1, 0, -2, 2], 0),
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
        )
        self.assertEqual(self.solution.fourSum([2, 2, 2, 2, 2], 8), [[2, 2, 2, 2]])
        self.assertEqual(self.solution.fourSum([0, 0, 0, 0], 0), [[0, 0, 0, 0]])

    def test_no_solution(self):
        self.assertEqual(self.solution.fourSum([1, 2, 3], 6), [])
        self.assertEqual(self.solution.fourSum([1, 2, 3, 4], 100), [])


if __name__ == "__main__":
    unittest.main()
