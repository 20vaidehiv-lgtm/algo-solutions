import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice311 import Solution  # noqa: E402


class MultiplyStringsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.multiply("2", "3"), "6")
        self.assertEqual(self.sol.multiply("123", "456"), "56088")

    def test_zero(self):
        self.assertEqual(self.sol.multiply("0", "99999"), "0")


if __name__ == "__main__":
    unittest.main()
