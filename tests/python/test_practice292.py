import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice292 import hurdleRace  # noqa: E402


class HurdleRaceTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(hurdleRace(7, [1, 6, 3, 5, 2]), 0)
        self.assertEqual(hurdleRace(4, [1, 6, 3, 5, 2]), 2)
        self.assertEqual(hurdleRace(2, [3, 5, 7, 9, 1]), 7)


if __name__ == "__main__":
    unittest.main()

