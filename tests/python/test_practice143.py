import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice143 import Solution  # noqa: E402


class SubsetsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(
            self.sol.subsets([1, 2, 3]),
            [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
        )
        self.assertEqual(self.sol.subsets([0]), [[], [0]])

    def test_empty(self):
        self.assertEqual(self.sol.subsets([]), [[]])


if __name__ == "__main__":
    unittest.main()
