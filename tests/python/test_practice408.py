import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice408 import countTriplets  # noqa: E402


class CountTripletsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(countTriplets([1, 2, 2, 4], 2), 2)
        self.assertEqual(countTriplets([1, 3, 9, 9, 27, 81], 3), 6)
        self.assertEqual(countTriplets([1, 5, 5, 25, 125], 5), 4)

    def test_edge_cases(self):
        self.assertEqual(countTriplets([1], 1), 0)
        self.assertEqual(countTriplets([1, 1, 1], 1), 1)
        self.assertEqual(countTriplets([1, 1, 1, 1], 1), 4)


if __name__ == "__main__":
    unittest.main()

