import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice244 import product_fib  # noqa: E402


class ProductFibTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(product_fib(4895), [55, 89, True])
        self.assertEqual(product_fib(5895), [89, 144, False])
        self.assertEqual(product_fib(0), [0, 1, True])
        self.assertEqual(product_fib(714), [21, 34, True])


if __name__ == "__main__":
    unittest.main()
