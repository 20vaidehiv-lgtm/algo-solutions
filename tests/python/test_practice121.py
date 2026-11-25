import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice121 import spiral_display  # noqa: E402


class SpiralDisplayTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(spiral_display([[1, 2, 3], [8, 9, 4], [7, 6, 5]]), "1 2 3 4 5 6 7 8 9")


if __name__ == "__main__":
    unittest.main()

