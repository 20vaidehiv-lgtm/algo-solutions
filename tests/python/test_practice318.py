import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice318 import Solution  # noqa: E402


class FindNumbersWithEvenDigitsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.findNumbers([12, 345, 2, 6, 7896]), 2)
        self.assertEqual(self.sol.findNumbers([555, 901, 482, 1771]), 1)

    def test_boundaries(self):
        self.assertEqual(self.sol.findNumbers([10, 99, 1000, 1]), 3)


if __name__ == "__main__":
    unittest.main()
