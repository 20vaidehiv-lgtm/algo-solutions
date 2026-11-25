import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice181 import Solution  # noqa: E402


class NextGreaterElementTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.nextGreaterElement([2, 4], [1, 2, 3, 4]), [3, -1])
        self.assertEqual(self.sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])
        self.assertEqual(
            self.sol.nextGreaterElement([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]),
            [7, 7, 7, 7, 7],
        )


if __name__ == "__main__":
    unittest.main()
