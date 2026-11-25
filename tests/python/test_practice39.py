import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice39 import betterDays  # noqa: E402


class BetterDaysTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(betterDays([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
        self.assertEqual(betterDays([30, 40, 50, 60]), [1, 1, 1, 0])
        self.assertEqual(betterDays([]), [])


if __name__ == "__main__":
    unittest.main()

