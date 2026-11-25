import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice154 import Solution  # noqa: E402


class RunningSumTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.runningSum([1, 2, 3, 4]), [1, 3, 6, 10])
        self.assertEqual(sol.runningSum([1, 1, 1, 1, 1]), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()

