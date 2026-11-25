import io
import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice397 import Solution  # noqa: E402


class CombinationSumTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        with patch("sys.stdout", io.StringIO()):
            self.assertCountEqual(
                self.solution.combinationSum([2, 3, 5], 8),
                [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
            )
            self.assertCountEqual(
                self.solution.combinationSum([2, 3, 6, 7], 7),
                [[2, 2, 3], [7]],
            )
            self.assertEqual(self.solution.combinationSum([2], 1), [])


if __name__ == "__main__":
    unittest.main()
