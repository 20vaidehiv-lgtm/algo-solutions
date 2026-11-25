import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice196 import comp  # noqa: E402


class CompTest(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(comp([1, 2, 3, 2], [1, 4, 9, 4]))
        self.assertTrue(
            comp(
                [121, 144, 19, 161, 19, 144, 19, 11],
                [121, 14641, 20736, 361, 25921, 361, 20736, 361],
            )
        )
        self.assertFalse(
            comp(
                [121, 144, 19, 161, 19, 144, 19, 11],
                [132, 14641, 20736, 361, 25921, 361, 20736, 361],
            )
        )
        self.assertFalse(comp([1, 2, 3], [1, 9]))

    def test_edge_cases(self):
        self.assertTrue(comp([], []))
        self.assertFalse(comp(None, []))
        self.assertFalse(comp([], None))


if __name__ == "__main__":
    unittest.main()
