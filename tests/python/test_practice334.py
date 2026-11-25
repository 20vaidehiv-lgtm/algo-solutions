import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice334 import Solution  # noqa: E402


class JumpGameIITest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.jumps([2, 3, 1, 1, 4]), 2)
        self.assertEqual(self.sol.jumps([2, 3, 0, 1, 4]), 2)
        self.assertEqual(self.sol.jumps([0]), 0)

    def test_step_by_step(self):
        self.assertEqual(self.sol.jumps([1, 1, 1, 1]), 3)


if __name__ == "__main__":
    unittest.main()
