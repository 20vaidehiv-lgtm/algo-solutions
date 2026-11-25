import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice226 import Solution  # noqa: E402


class FindRelativeRanksTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(
            self.solution.findRelativeRanks([5, 4, 3, 2, 1]),
            ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"],
        )
        self.assertEqual(
            self.solution.findRelativeRanks([10, 3, 8, 9, 4]),
            ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"],
        )
        self.assertEqual(
            self.solution.findRelativeRanks([1, 2, 3, 4, 5]),
            ["5", "4", "Bronze Medal", "Silver Medal", "Gold Medal"],
        )

    def test_fewer_than_three(self):
        self.assertEqual(self.solution.findRelativeRanks([10, 20]), ["Silver Medal", "Gold Medal"])
        self.assertEqual(self.solution.findRelativeRanks([7]), ["Gold Medal"])


if __name__ == "__main__":
    unittest.main()
