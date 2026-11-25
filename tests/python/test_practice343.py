import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice343 import Solution  # noqa: E402


class Sort012Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.sort012([0, 1, 2, 0, 1, 2]), [0, 0, 1, 1, 2, 2])
        self.assertEqual(self.sol.sort012([2, 1, 0, 2, 1, 0]), [0, 0, 1, 1, 2, 2])
        self.assertEqual(self.sol.sort012([0, 0, 1, 1, 2, 2]), [0, 0, 1, 1, 2, 2])

    def test_in_place_and_edge_cases(self):
        arr = [2, 0, 1]
        res = self.sol.sort012(arr)
        self.assertIs(res, arr)
        self.assertEqual(arr, [0, 1, 2])
        self.assertEqual(self.sol.sort012([]), [])


if __name__ == "__main__":
    unittest.main()
