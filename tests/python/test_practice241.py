import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice241 import Solution  # noqa: E402


class CountDigitOccurrencesTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(self.solution.countDigitOccurrences([12, 54, 32, 22], 2), 4)
        self.assertEqual(self.solution.countDigitOccurrences([3], 1), 0)
        self.assertEqual(self.solution.countDigitOccurrences([0, 10, 100], 0), 4)


if __name__ == "__main__":
    unittest.main()
