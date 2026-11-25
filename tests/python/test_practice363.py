import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice363 import Solution  # noqa: E402


class CombinationsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.combine(4, 2), [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])
        self.assertEqual(self.sol.combine(4, 3), [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]])
        self.assertEqual(self.sol.combine(4, 1), [[1], [2], [3], [4]])
        self.assertEqual(self.sol.combine(1, 1), [[1]])

    def test_k_zero(self):
        self.assertEqual(self.sol.combine(3, 0), [[]])


if __name__ == "__main__":
    unittest.main()
