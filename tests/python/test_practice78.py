import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice78 import sum_digits  # noqa: E402


class DigitalRootTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_digits(38), 2)
        self.assertEqual(sum_digits(999), 9)
        self.assertEqual(sum_digits(12345), 6)
        self.assertEqual(sum_digits(0), 0)


if __name__ == "__main__":
    unittest.main()

