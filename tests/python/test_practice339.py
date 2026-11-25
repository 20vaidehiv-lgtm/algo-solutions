import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice339 import Solution  # noqa: E402


class FindTheDifferenceTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.findTheDifference("abcd", "abcde"), "e")
        self.assertEqual(self.sol.findTheDifference("", "y"), "y")
        self.assertEqual(self.sol.findTheDifference("a", "aa"), "a")

    def test_shuffled_strings(self):
        self.assertEqual(self.sol.findTheDifference("ae", "aea"), "a")
        self.assertEqual(self.sol.findTheDifference("xyz", "zxqy"), "q")


if __name__ == "__main__":
    unittest.main()
