import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice373 import Solution  # noqa: E402


class RotateArrayByOneTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.rotate([1, 2, 3, 4, 5, 6, 7]), [7, 1, 2, 3, 4, 5, 6])
        self.assertEqual(self.sol.rotate([1, 2, 3, 4, 5, 6]), [6, 1, 2, 3, 4, 5])
        self.assertEqual(self.sol.rotate([1, 2, 3, 4, 5]), [5, 1, 2, 3, 4])

    def test_edge_cases(self):
        self.assertEqual(self.sol.rotate([]), [])
        self.assertEqual(self.sol.rotate([42]), [42])


if __name__ == "__main__":
    unittest.main()
