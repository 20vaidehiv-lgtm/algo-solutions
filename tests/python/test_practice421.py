import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice421 import build, min_depth  # noqa: E402


class MinDepthTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(min_depth(build([3, 9, 20, None, None, 15, 7])), 2)
        self.assertEqual(min_depth(build([1, 2, None, 3, None, 4, None, 5])), 5)

    def test_edge_cases(self):
        self.assertEqual(min_depth(None), 0)
        self.assertEqual(min_depth(build([1])), 1)


if __name__ == "__main__":
    unittest.main()

