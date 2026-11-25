import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice419 import sum_even_and_odd  # noqa: E402


class SumEvenAndOddTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_even_and_odd([1, 2, 3, 4]), (6, 4))
        self.assertEqual(sum_even_and_odd([0, -2, 5]), (-2, 5))


if __name__ == "__main__":
    unittest.main()

