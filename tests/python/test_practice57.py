import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice57 import canSplitString  # noqa: E402


class CanSplitStringTest(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(canSplitString("hello world"))
        self.assertFalse(canSplitString(""))
        self.assertFalse(canSplitString("   "))


if __name__ == "__main__":
    unittest.main()

