import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice328 import Solution  # noqa: E402


class MaxConsecutiveOnesTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)
        self.assertEqual(self.sol.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]), 2)

    def test_edge_cases(self):
        self.assertEqual(self.sol.findMaxConsecutiveOnes([0, 0, 0, 0, 0, 0]), 0)
        self.assertEqual(self.sol.findMaxConsecutiveOnes([]), 0)
        self.assertEqual(self.sol.findMaxConsecutiveOnes([1]), 1)


if __name__ == "__main__":
    unittest.main()
