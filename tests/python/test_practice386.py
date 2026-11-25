import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice386 import multiply_all  # noqa: E402


class MultiplyAllTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(multiply_all([1, 2, 3])(4), [4, 8, 12])
        self.assertEqual(multiply_all([1, 2, 3])(3), [3, 6, 9])
        self.assertEqual(multiply_all([1, 2, 3])(2), [2, 4, 6])

    def test_edge_cases(self):
        self.assertEqual(multiply_all([])(5), [])
        self.assertEqual(multiply_all([1, -2, 3])(0), [0, 0, 0])


if __name__ == "__main__":
    unittest.main()
