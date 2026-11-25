import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice23 import solution  # noqa: E402


class SmallestPossibleSumTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([6, 9, 21]), 9)
        self.assertEqual(solution([9]), 9)
        self.assertEqual(solution([1, 21, 55]), 3)


if __name__ == "__main__":
    unittest.main()

