import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice381 import up_array  # noqa: E402


class UpArrayTest(unittest.TestCase):
    def test_valid_arrays(self):
        self.assertEqual(up_array([4, 3, 2, 5]), [4, 3, 2, 6])
        self.assertEqual(up_array([9, 9, 9]), [1, 0, 0, 0])
        self.assertEqual(up_array([1, 2, 3]), [1, 2, 4])
        self.assertEqual(up_array([0]), [1])

    def test_invalid_or_empty_arrays(self):
        self.assertIsNone(up_array([1, -9]))
        self.assertIsNone(up_array([1, 10]))
        self.assertIsNone(up_array([]))


if __name__ == "__main__":
    unittest.main()
