import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice210 import multiplication_table  # noqa: E402


class MultiplicationTableTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(multiplication_table(1), [[1]])
        self.assertEqual(multiplication_table(2), [[1, 2], [2, 4]])
        self.assertEqual(multiplication_table(3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])

    def test_zero(self):
        self.assertEqual(multiplication_table(0), [])


if __name__ == "__main__":
    unittest.main()
