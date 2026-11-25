import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice345 import Solution  # noqa: E402


class CountEvenLettersTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.count("abcde"), 0)
        self.assertEqual(self.sol.count("aabbcde"), 2)
        self.assertEqual(self.sol.count("aabbccde"), 3)

    def test_edge_cases(self):
        self.assertEqual(self.sol.count(""), 0)
        self.assertEqual(self.sol.count("aaaa"), 1)


if __name__ == "__main__":
    unittest.main()
