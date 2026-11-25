import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice265 import Solution  # noqa: E402


class ArraySearchTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.search([1, 2, 3, 5, 6], 3), 2)
        self.assertEqual(sol.search([1, 2, 3], 9), -1)


if __name__ == "__main__":
    unittest.main()

