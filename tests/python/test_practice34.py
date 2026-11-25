import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice34 import sort012  # noqa: E402


class Sort012Test(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sort012([0, 1, 2, 0, 1, 2]), [0, 0, 1, 1, 2, 2])
        self.assertEqual(sort012([2, 1, 0]), [0, 1, 2])
        self.assertEqual(sort012([]), [])


if __name__ == "__main__":
    unittest.main()

