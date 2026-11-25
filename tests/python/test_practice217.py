import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice217 import data_reverse  # noqa: E402


class DataReverseTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            data_reverse([1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]),
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        )
        self.assertEqual(
            data_reverse([0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0]),
            [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
        )
        self.assertEqual(
            data_reverse([1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]),
            [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
        )

    def test_empty(self):
        self.assertEqual(data_reverse([]), [])


if __name__ == "__main__":
    unittest.main()
