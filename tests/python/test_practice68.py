import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice68 import generate_fibonacci  # noqa: E402


class GenerateFibonacciTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(generate_fibonacci(1), [0])
        self.assertEqual(generate_fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(generate_fibonacci(0), [])


if __name__ == "__main__":
    unittest.main()

