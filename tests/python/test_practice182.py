import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice182 import Solution  # noqa: E402


class NumberComplementTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.findComplement(5), 2)
        self.assertEqual(self.sol.findComplement(1), 0)
        self.assertEqual(self.sol.findComplement(12), 3)


if __name__ == "__main__":
    unittest.main()
