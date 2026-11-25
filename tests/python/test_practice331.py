import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice331 import circularArrayRotation  # noqa: E402


class CircularArrayRotationTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(circularArrayRotation([1, 2, 3, 4], 4, [0, 1, 2, 3]), [1, 2, 3, 4])
        self.assertEqual(circularArrayRotation([1, 2, 3], 2, [0, 1, 2]), [2, 3, 1])
        self.assertEqual(circularArrayRotation([3, 4, 5], 2, [1, 2]), [5, 3])

    def test_edge_cases(self):
        self.assertEqual(circularArrayRotation([1, 2, 3], 0, [0, 1, 2]), [1, 2, 3])
        self.assertEqual(circularArrayRotation([1, 2, 3, 4, 5], 7, [0, 3, 4]), [4, 2, 3])
        self.assertEqual(circularArrayRotation([9], 100, [0]), [9])


if __name__ == "__main__":
    unittest.main()
