import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice290 import findMedian  # noqa: E402


class FindMedianTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(findMedian([0, 1, 2, 4, 6, 5, 3]), 3)
        self.assertEqual(findMedian([5, 3, 1]), 3)


if __name__ == "__main__":
    unittest.main()

