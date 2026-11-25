import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice76 import Solution  # noqa: E402


class MySqrtTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.mySqrt(4), 2)
        self.assertEqual(sol.mySqrt(8), 2)
        self.assertEqual(sol.mySqrt(0), 0)
        self.assertEqual(sol.mySqrt(1), 1)


if __name__ == "__main__":
    unittest.main()

