import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice268 import Solution  # noqa: E402


class SelfDividingNumbersTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.selfDividingNumbers(1, 22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])
        self.assertEqual(sol.selfDividingNumbers(47, 85), [48, 55, 66, 77])


if __name__ == "__main__":
    unittest.main()

