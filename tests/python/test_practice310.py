import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice310 import nonDivisibleSubset  # noqa: E402


class NonDivisibleSubsetTest(unittest.TestCase):
    def test_examples(self):
        s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
        self.assertEqual(nonDivisibleSubset(7, s), 11)
        self.assertEqual(nonDivisibleSubset(3, [1, 7, 2, 4]), 3)

    def test_edge_cases(self):
        self.assertEqual(nonDivisibleSubset(1, [1, 2, 3]), 1)
        self.assertEqual(nonDivisibleSubset(4, [2, 2, 6, 10]), 1)


if __name__ == "__main__":
    unittest.main()
