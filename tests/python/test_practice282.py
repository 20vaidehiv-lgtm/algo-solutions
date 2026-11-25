import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice282 import findDigits  # noqa: E402


class FindDigitsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(findDigits(12), 2)
        self.assertEqual(findDigits(1012), 3)


if __name__ == "__main__":
    unittest.main()

