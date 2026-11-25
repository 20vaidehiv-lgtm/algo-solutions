import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice186 import Solution  # noqa: E402


class CountDigitsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.countDigits(7), 1)
        self.assertEqual(self.sol.countDigits(121), 2)
        self.assertEqual(self.sol.countDigits(1248), 4)

    def test_non_divisible_digits(self):
        self.assertEqual(self.sol.countDigits(23), 0)


if __name__ == "__main__":
    unittest.main()
