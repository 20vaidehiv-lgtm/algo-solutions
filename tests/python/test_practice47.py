import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice47 import rotate  # noqa: E402


class RotateListTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(rotate([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
        self.assertEqual(rotate([1, 2, 3, 4, 5], -1), [2, 3, 4, 5, 1])
        self.assertEqual(rotate([], 10), [])


if __name__ == "__main__":
    unittest.main()

