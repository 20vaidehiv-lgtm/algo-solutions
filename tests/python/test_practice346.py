import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice346 import Solution  # noqa: E402


class BinaryToDecimalTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.binary_to_decimal("101"), 5)
        self.assertEqual(self.sol.binary_to_decimal("1001"), 9)
        self.assertEqual(self.sol.binary_to_decimal("1111"), 15)

    def test_zero_and_large(self):
        self.assertEqual(self.sol.binary_to_decimal("0"), 0)
        self.assertEqual(self.sol.binary_to_decimal("100000"), 32)


if __name__ == "__main__":
    unittest.main()
