import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice254 import change  # noqa: E402


class CoinChangeTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(change(25), [20, 5])
        self.assertEqual(change(15), [10, 5])
        self.assertEqual(change(45), [20, 20, 5])


if __name__ == "__main__":
    unittest.main()

