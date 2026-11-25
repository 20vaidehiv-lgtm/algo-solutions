import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice169 import broke_count  # noqa: E402


class BrokeCountTest(unittest.TestCase):
    def test_weekly_and_three_day_streaks(self):
        self.assertEqual(broke_count([10] * 7), 1)
        self.assertEqual(broke_count([7, 7, 7]), 1)
        self.assertEqual(broke_count([10] * 7 + [7, 7, 7] + [3]), 3)

    def test_single_days_and_mixed(self):
        self.assertEqual(broke_count([3, 8, 3]), 2)
        self.assertEqual(broke_count([11, 12, 13]), 0)
        self.assertEqual(broke_count([]), 0)


if __name__ == "__main__":
    unittest.main()
