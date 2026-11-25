import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice305 import Solution  # noqa: E402


class SumOddLengthSubarraysTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.sumOddLengthSubarrays([1, 4, 2, 5, 3]), 58)
        self.assertEqual(self.sol.sumOddLengthSubarrays([10, 11, 12]), 66)
        self.assertEqual(self.sol.sumOddLengthSubarrays([1, 2]), 3)

    def test_single_element(self):
        self.assertEqual(self.sol.sumOddLengthSubarrays([5]), 5)


if __name__ == "__main__":
    unittest.main()
