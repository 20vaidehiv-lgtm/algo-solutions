import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice347 import Solution  # noqa: E402


class CountingBitsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.countBits(10), [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2])
        self.assertEqual(self.sol.countBits(5), [0, 1, 1, 2, 1, 2])
        self.assertEqual(self.sol.countBits(2), [0, 1, 1])

    def test_zero(self):
        self.assertEqual(self.sol.countBits(0), [0])


if __name__ == "__main__":
    unittest.main()
