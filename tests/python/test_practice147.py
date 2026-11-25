import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice147 import Solution  # noqa: E402


class FindPermutationDifferenceTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.findPermutationDifference("abc", "bac"), 2)
        self.assertEqual(self.sol.findPermutationDifference("abcde", "edbac"), 12)


if __name__ == "__main__":
    unittest.main()
