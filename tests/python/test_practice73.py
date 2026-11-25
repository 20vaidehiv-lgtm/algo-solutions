import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice73 import is_prime, nth_prime  # noqa: E402


class NthPrimeTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(nth_prime(1), 2)
        self.assertEqual(nth_prime(6), 13)
        self.assertIsNone(nth_prime(0))
        self.assertTrue(is_prime(29))


if __name__ == "__main__":
    unittest.main()

