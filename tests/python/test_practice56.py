import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice56 import number_power_sum  # noqa: E402


class NumberPowerSumTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(number_power_sum("123 2"), "941")
        self.assertEqual(number_power_sum("12 3"), "81")
        self.assertEqual(number_power_sum("10 1"), "01")


if __name__ == "__main__":
    unittest.main()

