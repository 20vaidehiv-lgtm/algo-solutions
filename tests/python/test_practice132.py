import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice132 import can_jump  # noqa: E402


class CanJumpTest(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(can_jump([2, 1, 3, 1, 0, 1]))
        self.assertFalse(can_jump([3, 2, 1, 0, 4]))

    def test_single_element(self):
        self.assertTrue(can_jump([0]))


if __name__ == "__main__":
    unittest.main()
