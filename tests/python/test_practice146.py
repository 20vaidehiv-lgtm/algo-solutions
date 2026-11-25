import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice146 import Solution  # noqa: E402


class NumberOfEmployeesWhoMetTargetTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.numberOfEmployeesWhoMetTarget([0, 1, 2, 3, 4], 2), 3)
        self.assertEqual(self.sol.numberOfEmployeesWhoMetTarget([5, 1, 4, 2, 2], 6), 0)


if __name__ == "__main__":
    unittest.main()
