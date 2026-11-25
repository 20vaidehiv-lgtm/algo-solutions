import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice401 import square_area  # noqa: E402


class SquareAreaTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(square_area(14.05), 80.0)
        self.assertEqual(square_area(2), 1.62)
        self.assertEqual(square_area(0), 0.0)


if __name__ == "__main__":
    unittest.main()

