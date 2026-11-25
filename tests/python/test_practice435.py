import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice435 import oranges_rotting  # noqa: E402


class RottingOrangesTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4)
        self.assertEqual(oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]), -1)
        self.assertEqual(oranges_rotting([[0, 2]]), 0)


if __name__ == "__main__":
    unittest.main()

