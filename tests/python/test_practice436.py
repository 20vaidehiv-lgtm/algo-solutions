import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice436 import min_eating_speed  # noqa: E402


class KokoEatingBananasTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_eating_speed([3, 6, 7, 11], 8), 4)
        self.assertEqual(min_eating_speed([30, 11, 23, 4, 20], 5), 30)
        self.assertEqual(min_eating_speed([30, 11, 23, 4, 20], 6), 23)

    def test_edge_cases(self):
        self.assertEqual(min_eating_speed([1], 1), 1)
        self.assertEqual(min_eating_speed([1000000000], 2), 500000000)


if __name__ == "__main__":
    unittest.main()

