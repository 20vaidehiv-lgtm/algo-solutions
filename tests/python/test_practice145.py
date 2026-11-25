import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice145 import Solution  # noqa: E402


class LeftRightDifferenceTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.leftRightDifference([10, 4, 8, 3]), [15, 1, 11, 22])
        self.assertEqual(self.sol.leftRightDifference([1]), [0])


if __name__ == "__main__":
    unittest.main()
