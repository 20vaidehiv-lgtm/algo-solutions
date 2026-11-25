import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice313 import Solution  # noqa: E402


class MapWordWeightsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        weights = [5, 3, 12, 14, 1, 2, 3, 2, 10, 6, 6, 9, 7, 8, 7, 10, 8, 9, 6, 9, 9, 8, 3, 7, 7, 2]
        self.assertEqual(self.sol.mapWordWeights(["abcd", "def", "xyz"], weights), "rij")

    def test_zero_weights(self):
        self.assertEqual(self.sol.mapWordWeights(["a", "bc"], [0] * 26), "zz")


if __name__ == "__main__":
    unittest.main()
