import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice42 import sum_multiples_3_5  # noqa: E402


class SumMultiplesTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_multiples_3_5(10), 23)
        self.assertEqual(sum_multiples_3_5(1000), 233168)
        self.assertEqual(sum_multiples_3_5(0), 0)


if __name__ == "__main__":
    unittest.main()

