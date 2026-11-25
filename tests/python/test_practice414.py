import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice414 import Solution  # noqa: E402


class GasStationTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)
        self.assertEqual(sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]), -1)


if __name__ == "__main__":
    unittest.main()

