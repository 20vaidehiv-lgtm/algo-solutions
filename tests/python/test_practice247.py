import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice247 import get_missing_element  # noqa: E402


class MissingElementTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(get_missing_element([0, 5, 1, 3, 2, 9, 7, 6, 4]), 8)
        self.assertEqual(get_missing_element([9, 2, 4, 5, 7, 0, 8, 6, 1]), 3)
        self.assertEqual(get_missing_element([9, 2, 4, 5, 3, 0, 8, 6, 1]), 7)
        self.assertEqual(get_missing_element([0, 1, 2, 3, 4, 5, 6, 7, 8]), 9)


if __name__ == "__main__":
    unittest.main()
