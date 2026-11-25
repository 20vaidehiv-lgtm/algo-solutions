import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice118 import is_prime  # noqa: E402


class IsPrimeTest(unittest.TestCase):
    def test_primes(self):
        for p in (2, 3, 5, 7, 11, 97):
            self.assertTrue(is_prime(p))

    def test_non_primes(self):
        for n in (-7, 0, 1, 4, 9, 15):
            self.assertFalse(is_prime(n))


if __name__ == "__main__":
    unittest.main()

