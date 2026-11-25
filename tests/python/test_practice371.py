import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice371 import Solution  # noqa: E402


class PowerOfTwoTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertTrue(self.sol.isPowerofTwo(1))
        self.assertTrue(self.sol.isPowerofTwo(8))
        self.assertFalse(self.sol.isPowerofTwo(98))

    def test_zero_and_large_power(self):
        self.assertFalse(self.sol.isPowerofTwo(0))
        self.assertTrue(self.sol.isPowerofTwo(1024))


if __name__ == "__main__":
    unittest.main()
