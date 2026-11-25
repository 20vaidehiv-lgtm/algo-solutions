import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice153 import Solution  # noqa: E402


class SmallerNumbersThanCurrentTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.smallerNumbersThanCurrent([8, 1, 2, 2, 3]), [4, 0, 1, 1, 3])
        self.assertEqual(sol.smallerNumbersThanCurrent([6, 5, 4, 8]), [2, 1, 0, 3])


if __name__ == "__main__":
    unittest.main()

