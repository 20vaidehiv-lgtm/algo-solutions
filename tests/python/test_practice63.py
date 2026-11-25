import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice63 import bigger_price  # noqa: E402


class BiggerPriceTest(unittest.TestCase):
    def test_examples(self):
        data = [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1},
        ]
        self.assertEqual(bigger_price(2, data), [{"name": "wine", "price": 138}, {"name": "bread", "price": 100}])


if __name__ == "__main__":
    unittest.main()

