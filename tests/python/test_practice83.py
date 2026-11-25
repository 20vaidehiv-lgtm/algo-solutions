import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice83 import evenNumberDigits  # noqa: E402


class EvenNumberDigitsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(evenNumberDigits([12, 345, 2, 6, 7896]), 2)
        self.assertEqual(evenNumberDigits([555, 901, 482, 1771]), 1)
        self.assertEqual(evenNumberDigits([]), 0)


if __name__ == "__main__":
    unittest.main()

