import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice199 import Solution  # noqa: E402


class CreateTargetArrayTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(
            self.sol.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]),
            [0, 4, 1, 3, 2],
        )
        self.assertEqual(
            self.sol.createTargetArray([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]),
            [0, 1, 2, 3, 4],
        )
        self.assertEqual(self.sol.createTargetArray([1], [0]), [1])


if __name__ == "__main__":
    unittest.main()
