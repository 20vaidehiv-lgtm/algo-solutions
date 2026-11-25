import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice350 import Solution  # noqa: E402


class RotateArrayTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.rotateArr([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2])
        self.assertEqual(self.sol.rotateArr([1, 2, 3, 4, 5], 3), [4, 5, 1, 2, 3])
        self.assertEqual(self.sol.rotateArr([1, 2, 3, 4, 5], 7), [3, 4, 5, 1, 2])

    def test_in_place_and_full_rotation(self):
        arr = [10, 20, 30]
        res = self.sol.rotateArr(arr, 3)
        self.assertIs(res, arr)
        self.assertEqual(arr, [10, 20, 30])


if __name__ == "__main__":
    unittest.main()
