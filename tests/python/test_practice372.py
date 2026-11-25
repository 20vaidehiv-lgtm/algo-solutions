import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice372 import Solution  # noqa: E402


class FloorSqrtTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.floorSqrt(4), 2)
        self.assertEqual(self.sol.floorSqrt(11), 3)
        self.assertEqual(self.sol.floorSqrt(25), 5)

    def test_one_and_non_perfect(self):
        self.assertEqual(self.sol.floorSqrt(1), 1)
        self.assertEqual(self.sol.floorSqrt(15), 3)


if __name__ == "__main__":
    unittest.main()
