import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice323 import Solution  # noqa: E402


class Maximum69NumberTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.maximum69Number(9999), 9999)
        self.assertEqual(self.sol.maximum69Number(9996), 9999)
        self.assertEqual(self.sol.maximum69Number(9669), 9969)

    def test_single_digit(self):
        self.assertEqual(self.sol.maximum69Number(6), 9)


if __name__ == "__main__":
    unittest.main()
