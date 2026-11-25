import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice177 import Solution  # noqa: E402


class WaterBottlesTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.numWaterBottles(9, 3), 13)
        self.assertEqual(self.sol.numWaterBottles(15, 4), 19)

    def test_no_exchange(self):
        self.assertEqual(self.sol.numWaterBottles(2, 3), 2)
        self.assertEqual(self.sol.numWaterBottles(0, 3), 0)


if __name__ == "__main__":
    unittest.main()
