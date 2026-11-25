import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice266 import Solution  # noqa: E402


class NextGreaterElementTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.nextGreaterElement([2, 4], [1, 2, 3, 4]), [3, -1])
        self.assertEqual(sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])


if __name__ == "__main__":
    unittest.main()

