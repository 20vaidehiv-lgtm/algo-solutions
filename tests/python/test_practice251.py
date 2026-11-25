import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice251 import fizzbuzzpop  # noqa: E402


class FizzBuzzPopTest(unittest.TestCase):
    def test_divisibility(self):
        self.assertEqual(fizzbuzzpop(9), "Fizz")
        self.assertEqual(fizzbuzzpop(10), "Buzz")
        self.assertEqual(fizzbuzzpop(15), "FizzBuzz")
        self.assertEqual(fizzbuzzpop(49), "Pop")
        self.assertEqual(fizzbuzzpop(105), "FizzBuzzPop")
        self.assertEqual(fizzbuzzpop(2), "")


if __name__ == "__main__":
    unittest.main()
