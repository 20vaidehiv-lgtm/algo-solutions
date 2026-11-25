import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice54 import averageWithoutMinMax  # noqa: E402


class AverageWithoutMinMaxTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(averageWithoutMinMax([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(averageWithoutMinMax([0, 1, 2, 3, 4, 5]), 2.5)
        self.assertEqual(averageWithoutMinMax([1, 2]), 0.0)


if __name__ == "__main__":
    unittest.main()

