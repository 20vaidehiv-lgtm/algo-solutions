import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice32 import Solution  # noqa: E402


class MaxProfitTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(sol.maxProfit([7, 6, 4, 3, 1]), 0)
        self.assertEqual(sol.maxProfit([1]), 0)


if __name__ == "__main__":
    unittest.main()

