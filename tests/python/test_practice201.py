import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice201 import Solution  # noqa: E402


class NumberOfStepsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.numberOfSteps(14), 6)
        self.assertEqual(self.sol.numberOfSteps(8), 4)
        self.assertEqual(self.sol.numberOfSteps(123), 12)

    def test_zero(self):
        self.assertEqual(self.sol.numberOfSteps(0), 0)


if __name__ == "__main__":
    unittest.main()
