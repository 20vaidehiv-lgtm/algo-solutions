import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice286 import migratoryBirds  # noqa: E402


class MigratoryBirdsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]), 3)
        self.assertEqual(migratoryBirds([1, 4, 4, 4, 5, 3]), 4)
        self.assertEqual(migratoryBirds([1, 1, 2, 2, 3]), 1)


if __name__ == "__main__":
    unittest.main()

