import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice233 import Solution  # noqa: E402


class SmallestRangeITest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(self.solution.smallestRangeI([1], 0), 0)
        self.assertEqual(self.solution.smallestRangeI([0, 10], 2), 6)
        self.assertEqual(self.solution.smallestRangeI([1, 3, 6], 3), 0)


if __name__ == "__main__":
    unittest.main()
