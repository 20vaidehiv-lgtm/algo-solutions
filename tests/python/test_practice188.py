import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice188 import Solution  # noqa: E402


class CountGoodTripletsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3), 4)
        self.assertEqual(self.sol.countGoodTriplets([1, 1, 2, 2, 3], 0, 0, 1), 0)


if __name__ == "__main__":
    unittest.main()
