import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice297 import pickingNumbers  # noqa: E402


class PickingNumbersTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(pickingNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5]), 5)
        self.assertEqual(pickingNumbers([4, 6, 5, 3, 3, 1]), 3)
        self.assertEqual(pickingNumbers([1, 2, 2, 3, 1, 2]), 5)

    def test_edge_cases(self):
        self.assertEqual(pickingNumbers([2, 2, 2]), 3)
        self.assertEqual(pickingNumbers([1, 10]), 1)


if __name__ == "__main__":
    unittest.main()
