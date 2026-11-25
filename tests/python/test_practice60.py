import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice60 import Solution  # noqa: E402


class PascalsTriangleTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.generate(1), [[1]])
        self.assertEqual(sol.generate(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])


if __name__ == "__main__":
    unittest.main()

