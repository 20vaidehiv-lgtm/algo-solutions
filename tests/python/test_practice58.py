import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice58 import backspaceStringCompare  # noqa: E402


class BackspaceStringCompareTest(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(backspaceStringCompare("ab#c", "ad#c"))
        self.assertTrue(backspaceStringCompare("ab##", "c#d#"))
        self.assertFalse(backspaceStringCompare("a#c", "b"))


if __name__ == "__main__":
    unittest.main()

