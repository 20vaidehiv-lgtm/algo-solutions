import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice134 import three_sum  # noqa: E402


class ThreeSumTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(three_sum([-1, 2, 1, -4], 1), 2)
        self.assertEqual(three_sum([0, 0, 0], 1), 0)


if __name__ == "__main__":
    unittest.main()
