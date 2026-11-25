import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice253 import islands  # noqa: E402


class IslandsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(islands([["1", "0", "1"], ["1", "1", "1"], ["1", "0", "1"]]), 7)
        self.assertEqual(islands([["0", "0"], ["0", "0"]]), 0)


if __name__ == "__main__":
    unittest.main()

