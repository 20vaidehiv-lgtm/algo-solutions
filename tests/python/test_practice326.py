import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice326 import Solution  # noqa: E402


class MinimumSumFourDigitTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.minimumSum(2932), 52)
        self.assertEqual(self.sol.minimumSum(4009), 13)
        self.assertEqual(self.sol.minimumSum(2687), 95)

    def test_all_same_digits(self):
        self.assertEqual(self.sol.minimumSum(1111), 22)


if __name__ == "__main__":
    unittest.main()
