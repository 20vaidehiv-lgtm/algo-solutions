import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice222 import cube_odd  # noqa: E402


class CubeOddTest(unittest.TestCase):
    def test_valid_arrays(self):
        self.assertEqual(cube_odd([1, 2, 3, 4, 5]), 153)
        self.assertEqual(cube_odd([-3, -2, 2, 3]), 0)
        self.assertEqual(cube_odd([2, 4, 6]), 0)
        self.assertEqual(cube_odd([]), 0)

    def test_non_int_elements(self):
        self.assertIsNone(cube_odd([0, 1, False, 3, True, 5]))
        self.assertIsNone(cube_odd([1, 2, 3, 4, 5, "7"]))
        self.assertIsNone(cube_odd([1, 2.0]))


if __name__ == "__main__":
    unittest.main()
