import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice229 import nth_fib  # noqa: E402


class NthFibTest(unittest.TestCase):
    def test_fibonacci_sequence(self):
        self.assertEqual(nth_fib(1), 0)
        self.assertEqual(nth_fib(2), 1)
        self.assertEqual(nth_fib(3), 1)
        self.assertEqual(nth_fib(4), 2)
        self.assertEqual(nth_fib(10), 34)
        self.assertEqual(nth_fib(100), 218922995834555169026)


if __name__ == "__main__":
    unittest.main()
