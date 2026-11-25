import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice24 import find_even_index  # noqa: E402


class EqualSidesTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(find_even_index([1, 2, 3, 4, 3, 2, 1]), 3)
        self.assertEqual(find_even_index([1, 2, 3, 4, 5, 6]), -1)


if __name__ == "__main__":
    unittest.main()

