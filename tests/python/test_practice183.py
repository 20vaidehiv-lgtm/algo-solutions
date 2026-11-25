import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice183 import Solution  # noqa: E402


class MinBitFlipsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.minBitFlips(10, 7), 3)
        self.assertEqual(self.sol.minBitFlips(3, 4), 3)

    def test_equal_numbers(self):
        self.assertEqual(self.sol.minBitFlips(8, 8), 0)
        self.assertEqual(self.sol.minBitFlips(0, 15), 4)


if __name__ == "__main__":
    unittest.main()
