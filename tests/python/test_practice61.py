import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice61 import getMaxTwice  # noqa: E402


class DominantIndexTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(getMaxTwice([3, 6, 1, 0]), 1)
        self.assertEqual(getMaxTwice([1, 2, 3, 4]), -1)
        self.assertEqual(getMaxTwice([1]), -1)


if __name__ == "__main__":
    unittest.main()

