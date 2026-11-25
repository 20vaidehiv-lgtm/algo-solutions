import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice191 import Solution  # noqa: E402


class GcdOfOddEvenSumsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.gcdOfOddEvenSums(5), 5)
        self.assertEqual(self.sol.gcdOfOddEvenSums(6), 6)
        self.assertEqual(self.sol.gcdOfOddEvenSums(1), 1)


if __name__ == "__main__":
    unittest.main()
