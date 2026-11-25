import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice276 import Solution  # noqa: E402


class NumberOfLinesTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.numberOfLines([10] * 26, "abcdefghijklmnopqrstuvwxyz"), [3, 60])
        self.assertEqual(sol.numberOfLines([4] + [10] * 25, "bbbcccdddaaa"), [2, 4])


if __name__ == "__main__":
    unittest.main()

