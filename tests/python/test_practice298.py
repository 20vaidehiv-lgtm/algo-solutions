import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice298 import getTotalX  # noqa: E402


class BetweenTwoSetsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(getTotalX([2, 4], [16, 32, 96]), 3)
        self.assertEqual(getTotalX([2, 6], [24, 36]), 2)

    def test_edge_cases(self):
        self.assertEqual(getTotalX([3, 4], [24, 48]), 2)
        self.assertEqual(getTotalX([1], [100]), 9)


if __name__ == "__main__":
    unittest.main()
