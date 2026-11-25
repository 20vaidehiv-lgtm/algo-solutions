import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice225 import Solution  # noqa: E402


class FindMatrixTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(
            self.solution.findMatrix([1, 3, 4, 1, 2, 3, 1]),
            [[1, 3, 4, 2], [1, 3], [1]],
        )
        self.assertEqual(
            self.solution.findMatrix([1, 1, 1, 1, 1]),
            [[1], [1], [1], [1], [1]],
        )
        self.assertEqual(self.solution.findMatrix([1, 2, 3, 4]), [[1, 2, 3, 4]])

    def test_empty(self):
        self.assertEqual(self.solution.findMatrix([]), [])


if __name__ == "__main__":
    unittest.main()
