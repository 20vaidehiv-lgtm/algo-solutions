import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice185 import Solution  # noqa: E402


class SumOfMultiplesTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.sumOfMultiples(7), 21)
        self.assertEqual(self.sol.sumOfMultiples(10), 40)
        self.assertEqual(self.sol.sumOfMultiples(9), 30)

    def test_small_values(self):
        self.assertEqual(self.sol.sumOfMultiples(1), 0)
        self.assertEqual(self.sol.sumOfMultiples(3), 3)


if __name__ == "__main__":
    unittest.main()
