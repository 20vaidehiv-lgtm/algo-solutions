import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice148 import Solution  # noqa: E402


class KidsWithCandiesTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.kidsWithCandies([2, 3, 5, 1, 3], 3), [True, True, True, False, True])
        self.assertEqual(sol.kidsWithCandies([4, 2, 1, 1, 2], 1), [True, False, False, False, False])


if __name__ == "__main__":
    unittest.main()

