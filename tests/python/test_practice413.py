import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice413 import Solution  # noqa: E402


class DailyTemperaturesTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
        self.assertEqual(sol.dailyTemperatures([30, 40, 50, 60]), [1, 1, 1, 0])


if __name__ == "__main__":
    unittest.main()

