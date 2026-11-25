import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice66 import sum_of_multiples  # noqa: E402


class SumOfMultiplesTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_of_multiples(10), 40)
        self.assertEqual(sum_of_multiples(1), 0)
        self.assertEqual(sum_of_multiples(7), 21)


if __name__ == "__main__":
    unittest.main()

