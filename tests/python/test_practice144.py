import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice144 import Solution  # noqa: E402


class ArrayPairSumTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.arrayPairSum([1, 4, 3, 2]), 4)
        self.assertEqual(self.sol.arrayPairSum([6, 2, 6, 5, 1, 2]), 9)


if __name__ == "__main__":
    unittest.main()
