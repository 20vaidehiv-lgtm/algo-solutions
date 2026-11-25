import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice295 import utopianTree  # noqa: E402


class UtopianTreeTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(utopianTree(0), 1)
        self.assertEqual(utopianTree(1), 2)
        self.assertEqual(utopianTree(3), 6)
        self.assertEqual(utopianTree(4), 7)
        self.assertEqual(utopianTree(5), 14)

    def test_more_cycles(self):
        self.assertEqual(utopianTree(2), 3)
        self.assertEqual(utopianTree(6), 15)


if __name__ == "__main__":
    unittest.main()
