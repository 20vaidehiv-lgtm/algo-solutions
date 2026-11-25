import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice364 import Solution  # noqa: E402


class ValidNumberTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertTrue(self.sol.isNumber(" 005047e+6"))
        self.assertFalse(self.sol.isNumber("95a54e53"))
        self.assertTrue(self.sol.isNumber("+6e-1"))
        self.assertFalse(self.sol.isNumber("."))

    def test_inf_nan_rejected(self):
        self.assertFalse(self.sol.isNumber("inf"))
        self.assertFalse(self.sol.isNumber("-Infinity"))
        self.assertFalse(self.sol.isNumber("NaN"))
        self.assertTrue(self.sol.isNumber("-.5"))


if __name__ == "__main__":
    unittest.main()
