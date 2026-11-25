import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice12 import Solution  # noqa: E402


class ReverseStrTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.reverseStr("abcdefg", 2), "bacdfeg")
        self.assertEqual(self.sol.reverseStr("abcd", 2), "bacd")
        self.assertEqual(self.sol.reverseStr("abcdefgh", 3), "cbadefhg")

    def test_edge_cases(self):
        self.assertEqual(self.sol.reverseStr("", 1), "")
        self.assertEqual(self.sol.reverseStr("a", 1), "a")
        self.assertEqual(self.sol.reverseStr("ab", 3), "ba")
        self.assertEqual(self.sol.reverseStr("abcdef", 4), "dcbaef")


if __name__ == "__main__":
    unittest.main()
