import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice423 import trap  # noqa: E402


class TrapRainWaterTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
        self.assertEqual(trap([4, 2, 0, 3, 2, 5]), 9)

    def test_no_water(self):
        self.assertEqual(trap([]), 0)
        self.assertEqual(trap([3, 2, 1]), 0)


if __name__ == "__main__":
    unittest.main()
