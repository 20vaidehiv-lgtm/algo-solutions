import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice6 import canJump  # noqa: E402


class CanJumpTest(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(canJump([2, 3, 1, 1, 4]))
        self.assertFalse(canJump([3, 2, 1, 0, 4]))

    def test_edge_cases(self):
        self.assertFalse(canJump([]))
        self.assertTrue(canJump([0]))
        self.assertTrue(canJump([1, 0]))
        self.assertFalse(canJump([0, 1]))
        self.assertTrue(canJump([2, 0, 0]))


if __name__ == "__main__":
    unittest.main()
