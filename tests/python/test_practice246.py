import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice246 import zeros  # noqa: E402


class TrailingZerosTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(zeros(0), 0)
        self.assertEqual(zeros(6), 1)
        self.assertEqual(zeros(30), 7)
        self.assertEqual(zeros(1000000000), 249999998)


if __name__ == "__main__":
    unittest.main()
