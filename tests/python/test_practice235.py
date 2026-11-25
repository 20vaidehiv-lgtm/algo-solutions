import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice235 import Solution  # noqa: E402


class SubarraySumTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(self.solution.subarraySum([2, 3, 1]), 11)
        self.assertEqual(self.solution.subarraySum([3, 1, 1, 2]), 13)

    def test_single_element(self):
        self.assertEqual(self.solution.subarraySum([5]), 5)


if __name__ == "__main__":
    unittest.main()
