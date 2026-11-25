import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice165 import Solution  # noqa: E402


class SubarraySumTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.subarraySum([1, 1, 1], 2), 2)
        self.assertEqual(sol.subarraySum([1, 2, 3], 3), 2)


if __name__ == "__main__":
    unittest.main()

