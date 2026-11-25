import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice29 import pow_sum_dig_term  # noqa: E402


class DigitPowerSumTest(unittest.TestCase):
    def test_first_terms(self):
        self.assertEqual(pow_sum_dig_term(1), 81)
        self.assertEqual(pow_sum_dig_term(2), 512)


if __name__ == "__main__":
    unittest.main()

