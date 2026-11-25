import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice262 import Solution  # noqa: E402


class FindIntersectionValuesTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.findIntersectionValues([4, 3, 2, 3, 1], [2, 2, 5, 2, 3, 6]), [3, 4])
        self.assertEqual(sol.findIntersectionValues([3, 4, 2, 3], [1, 5]), [0, 0])


if __name__ == "__main__":
    unittest.main()

