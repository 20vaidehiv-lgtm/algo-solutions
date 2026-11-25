import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice242 import Solution  # noqa: E402


class HeightCheckerTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(self.solution.heightChecker([1, 1, 4, 2, 1, 3]), 3)
        self.assertEqual(self.solution.heightChecker([5, 1, 2, 3, 4]), 5)
        self.assertEqual(self.solution.heightChecker([1, 2, 3, 4, 5]), 0)


if __name__ == "__main__":
    unittest.main()
