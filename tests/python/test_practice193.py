import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice193 import calculate  # noqa: E402


class CancellableItemTransactionsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(calculate({"A": 1, "B": 3, "C": 2}, "1A2BA3AC4CA"), 14)
        self.assertEqual(calculate({"X": 0, "Y": 0, "Z": 0}, "5X6Y20Z1X6Y"), 0)
        self.assertEqual(calculate({"R": 1, "Q": 2, "E": 3, "X": 4}, "4R1Q4X2E1R2X"), 37)
        self.assertEqual(calculate({"T": 12, "F": 6}, "2F5T1T"), 84)

    def test_negative_quantities_and_extra_cancel(self):
        self.assertEqual(calculate({"A": 5}, "-2A3AA"), -10)


if __name__ == "__main__":
    unittest.main()
