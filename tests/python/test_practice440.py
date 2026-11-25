import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice440 import calculate_span  # noqa: E402


class StockSpanTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(calculate_span([100, 80, 60, 70, 60, 75, 85]), [1, 1, 1, 2, 1, 4, 6])
        self.assertEqual(calculate_span([10, 4, 5, 90, 120, 80]), [1, 1, 2, 4, 5, 1])
        self.assertEqual(calculate_span([10, 10, 10]), [1, 2, 3])
        self.assertEqual(calculate_span([20, 15, 15, 10, 25]), [1, 1, 2, 1, 5])


if __name__ == "__main__":
    unittest.main()

