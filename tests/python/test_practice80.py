import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice80 import sol  # noqa: E402


class AllArraysSameElementsTest(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(sol([[1, 2, 3], [3, 1, 2], [2, 3, 1]]))
        self.assertFalse(sol([[1, 2, 3], [3, 1, 2], [2, 3, 4]]))
        self.assertTrue(sol([]))


if __name__ == "__main__":
    unittest.main()

