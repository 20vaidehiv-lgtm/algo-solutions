import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice21 import smallest_even_multiple  # noqa: E402


class SmallestEvenMultipleTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(smallest_even_multiple(4), 4)
        self.assertEqual(smallest_even_multiple(7), 14)
        self.assertEqual(smallest_even_multiple(10), 10)
        self.assertEqual(smallest_even_multiple(15), 30)

    def test_edge_cases(self):
        self.assertEqual(smallest_even_multiple(1), 2)
        self.assertEqual(smallest_even_multiple(0), 0)
        self.assertEqual(smallest_even_multiple(-3), 0)


if __name__ == "__main__":
    unittest.main()
