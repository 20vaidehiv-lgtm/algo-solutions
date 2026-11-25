import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice411 import Solution  # noqa: E402


class DigitFrequencyScoreTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.digitFrequencyScore(122), 5)
        self.assertEqual(sol.digitFrequencyScore(101), 2)
        self.assertEqual(sol.digitFrequencyScore(9999), 36)


if __name__ == "__main__":
    unittest.main()

