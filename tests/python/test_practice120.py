import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice120 import fibonacciEvenSum  # noqa: E402


class FibonacciEvenSumTest(unittest.TestCase):
    def test_euler_limit(self):
        self.assertEqual(fibonacciEvenSum(4_000_000), 4613732)
        self.assertEqual(fibonacciEvenSum(10), 10)


if __name__ == "__main__":
    unittest.main()

