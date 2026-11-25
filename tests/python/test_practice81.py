import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice81 import Solution1, Solution2  # noqa: E402


class FibonacciNumberTest(unittest.TestCase):
    def test_examples(self):
        for cls in (Solution1, Solution2):
            sol = cls()
            self.assertEqual(sol.fib(0), 0)
            self.assertEqual(sol.fib(1), 1)
            self.assertEqual(sol.fib(10), 55)


if __name__ == "__main__":
    unittest.main()

