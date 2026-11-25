import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice269 import stock_list  # noqa: E402


class StockListTest(unittest.TestCase):
    def test_examples(self):
        b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
        c = ["A", "B"]
        self.assertEqual(stock_list(b, c), "(A : 200) - (B : 1140)")
        self.assertEqual(stock_list([], c), "")


if __name__ == "__main__":
    unittest.main()

