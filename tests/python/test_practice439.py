# Note: solutions/python/practice439.py is currently marked IN PROGRESS.
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice439 import largest_prime_factor  # noqa: E402


class LargestPrimeFactorTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(18), 3)
        self.assertEqual(largest_prime_factor(100), 5)
        self.assertEqual(largest_prime_factor(600851475143), 6857)
        self.assertEqual(largest_prime_factor(8), 2)


if __name__ == "__main__":
    unittest.main()

