import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice3 import calculate_cable_length  # noqa: E402


class CalculateCableLengthTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(calculate_cable_length([(0, 0), (1, 1), (2, 2)]), 2)
        self.assertEqual(calculate_cable_length([(0, 0), (5, 0), (10, 0)]), 10)
        self.assertEqual(calculate_cable_length([(1, 1), (2, 2), (3, 3), (4, 4)]), 3)

    def test_edge_cases(self):
        self.assertEqual(calculate_cable_length([(0, 0)]), 0)
        self.assertEqual(calculate_cable_length([]), 0)
        self.assertEqual(calculate_cable_length([(-3, 5), (4, -2)]), 7)


if __name__ == "__main__":
    unittest.main()
