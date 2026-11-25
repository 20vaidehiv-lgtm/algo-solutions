import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice315 import Solution  # noqa: E402


class CountAndSayTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.countAndSay(1), "1")
        self.assertEqual(self.sol.countAndSay(4), "1211")

    def test_more_terms(self):
        self.assertEqual(self.sol.countAndSay(2), "11")
        self.assertEqual(self.sol.countAndSay(3), "21")
        self.assertEqual(self.sol.countAndSay(5), "111221")


if __name__ == "__main__":
    unittest.main()
