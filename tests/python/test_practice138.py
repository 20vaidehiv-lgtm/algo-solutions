import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice138 import calc  # noqa: E402


class CharCodeCalculationTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(calc("ABC"), 6)
        self.assertEqual(calc("abcdef"), 6)
        self.assertEqual(calc("aaaaaddddr"), 30)

    def test_no_sevens(self):
        self.assertEqual(calc("a"), 0)


if __name__ == "__main__":
    unittest.main()
