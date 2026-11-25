import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice351 import Solution  # noqa: E402


class SmallestPositiveMissingTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.missingNumber([7, 8, 9, 11, 12]), 1)
        self.assertEqual(self.sol.missingNumber([3, 4, -1, 1]), 2)
        self.assertEqual(self.sol.missingNumber([1, 2, 0]), 3)
        self.assertEqual(self.sol.missingNumber([-12, 0]), 1)

    def test_duplicates_and_empty(self):
        self.assertEqual(self.sol.missingNumber([1, 1, 2, 2]), 3)
        self.assertEqual(self.sol.missingNumber([]), 1)


if __name__ == "__main__":
    unittest.main()
