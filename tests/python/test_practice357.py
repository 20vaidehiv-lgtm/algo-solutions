import io
import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice357 import fairRations  # noqa: E402


class FairRationsTest(unittest.TestCase):
    def test_examples(self):
        with patch("sys.stdout", new=io.StringIO()):
            self.assertEqual(fairRations([2, 3, 4, 5, 6]), 4)
            self.assertEqual(fairRations([1, 2]), "NO")

    def test_already_even(self):
        with patch("sys.stdout", new=io.StringIO()):
            self.assertEqual(fairRations([2, 4, 6]), 0)


if __name__ == "__main__":
    unittest.main()
