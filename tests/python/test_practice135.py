import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice135 import remove_duplicates  # noqa: E402


class RemoveDuplicatesTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(remove_duplicates([1, 1, 2]), 2)
        self.assertEqual(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)

    def test_empty(self):
        self.assertEqual(remove_duplicates([]), 0)


if __name__ == "__main__":
    unittest.main()
