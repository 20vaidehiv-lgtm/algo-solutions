import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice300 import equalizeArray  # noqa: E402


class EqualizeArrayTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(equalizeArray([3, 3, 2, 1, 3]), 2)
        self.assertEqual(equalizeArray([1, 2, 3, 1, 2, 3, 3, 3]), 4)

    def test_edge_cases(self):
        self.assertEqual(equalizeArray([1, 1, 1]), 0)
        self.assertEqual(equalizeArray([5]), 0)


if __name__ == "__main__":
    unittest.main()
