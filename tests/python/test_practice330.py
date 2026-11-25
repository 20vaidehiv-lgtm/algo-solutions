import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice330 import Solution  # noqa: E402


class FindDifferenceTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        res1 = [sorted(x) for x in self.sol.findDifference([1, 2, 3], [2, 4, 6])]
        self.assertEqual(res1, [[1, 3], [4, 6]])

        res2 = [sorted(x) for x in self.sol.findDifference([1, 2, 3, 3], [1, 1, 2, 2])]
        self.assertEqual(res2, [[3], []])

        res3 = [sorted(x) for x in self.sol.findDifference([1, 2, 3], [1, 2, 3])]
        self.assertEqual(res3, [[], []])


if __name__ == "__main__":
    unittest.main()
