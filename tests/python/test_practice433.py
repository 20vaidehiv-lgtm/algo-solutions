import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice433 import min_jumps  # noqa: E402


class MinJumpsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]), 3)
        self.assertEqual(min_jumps([1, 4, 3, 2, 6, 7]), 2)

    def test_unreachable_and_single(self):
        self.assertEqual(min_jumps([0, 10, 20]), -1)
        self.assertEqual(min_jumps([1]), 0)


if __name__ == "__main__":
    unittest.main()

