import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice337 import Solution  # noqa: E402


class MergeIntervalsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(
            self.sol.merge([[1, 3], [2, 7], [8, 10], [15, 18], [17, 23], [3, 4], [4, 5], [10, 14], [11, 12], [13, 14]]),
            [[1, 7], [8, 14], [15, 23]],
        )
        self.assertEqual(self.sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])
        self.assertEqual(self.sol.merge([[1, 4], [4, 5]]), [[1, 5]])

    def test_unsorted_and_empty(self):
        self.assertEqual(self.sol.merge([[4, 7], [1, 4]]), [[1, 7]])
        self.assertEqual(self.sol.merge([]), [])
        self.assertEqual(self.sol.merge([[1, 5], [2, 3]]), [[1, 5]])


if __name__ == "__main__":
    unittest.main()
