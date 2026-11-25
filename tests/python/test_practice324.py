import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice324 import Solution  # noqa: E402


class SumIndicesWithKSetBitsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.sumIndicesWithKSetBits([5, 10, 1, 5, 2], 1), 13)
        self.assertEqual(self.sol.sumIndicesWithKSetBits([4, 3, 2, 1], 2), 1)

    def test_zero_set_bits(self):
        self.assertEqual(self.sol.sumIndicesWithKSetBits([10, 20, 30], 0), 10)


if __name__ == "__main__":
    unittest.main()
