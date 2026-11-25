import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice366 import Solution  # noqa: E402


class ReverseBitsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.reverseBits(43261596), 964176192)
        self.assertEqual(self.sol.reverseBits(2147483644), 1073741822)

    def test_edge_cases(self):
        self.assertEqual(self.sol.reverseBits(0), 0)
        self.assertEqual(self.sol.reverseBits(1), 1 << 31)


if __name__ == "__main__":
    unittest.main()
