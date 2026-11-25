import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice312 import Solution  # noqa: E402


class SortColorsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        nums = [2, 0, 2, 1, 1, 0]
        self.assertEqual(self.sol.sortColors(nums), [0, 0, 1, 1, 2, 2])
        self.assertEqual(self.sol.sortColors([2, 0, 1]), [0, 1, 2])

    def test_single_element(self):
        self.assertEqual(self.sol.sortColors([0]), [0])


if __name__ == "__main__":
    unittest.main()
