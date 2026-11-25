import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice319 import Solution  # noqa: E402


class RemoveTrailingZerosTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.removeTrailingZeros("51230100"), "512301")
        self.assertEqual(self.sol.removeTrailingZeros("123"), "123")

    def test_all_trailing_zeros(self):
        self.assertEqual(self.sol.removeTrailingZeros("1000"), "1")


if __name__ == "__main__":
    unittest.main()
