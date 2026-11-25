import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice375 import fizzbuzz_plusplus  # noqa: E402


class FizzBuzzPlusPlusTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            fizzbuzz_plusplus([3, 5], ["Fizz", "Buzz"]),
            [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"],
        )
        res3 = fizzbuzz_plusplus([2, 3, 5], ["Fizz", "Buzz", "Bang"])
        self.assertEqual(len(res3), 30)
        self.assertEqual(res3[:15], [1, "Fizz", "Buzz", "Fizz", "Bang", "FizzBuzz", 7, "Fizz", "Buzz", "FizzBang", 11, "Fizz", 13, "FizzBuzz", "Bang"])
        self.assertEqual(res3[-1], "FizzBuzzBang")

    def test_four_divisors_length(self):
        res4 = fizzbuzz_plusplus([2, 3, 5, 7], ["Fizz", "Buzz", "Bang", "Boom"])
        self.assertEqual(len(res4), 210)
        self.assertEqual(res4[209], "FizzBuzzBangBoom")


if __name__ == "__main__":
    unittest.main()
