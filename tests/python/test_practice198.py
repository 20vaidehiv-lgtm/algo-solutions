import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice198 import Solution  # noqa: E402


class NumberOfPairsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.numberOfPairs([1, 2, 3, 4], [1, 2, 3, 4], 1), 8)
        self.assertEqual(self.sol.numberOfPairs([1, 2, 3, 4], [1, 2, 3, 4], 2), 3)
        self.assertEqual(self.sol.numberOfPairs([1, 2, 3, 4], [1, 2, 3, 4], 3), 1)
        self.assertEqual(self.sol.numberOfPairs([1, 3, 4], [1, 3, 4], 1), 5)


if __name__ == "__main__":
    unittest.main()
