import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice250 import maxSub  # noqa: E402


class MaxSubTest(unittest.TestCase):
    def test_examples_and_empty(self):
        self.assertEqual(maxSub([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(maxSub([1, 2, 3, 4, 1, 7, 8, 9]), [1, 7, 8, 9])
        self.assertEqual(maxSub([10, 5, 2, 3]), [10])
        self.assertEqual(maxSub([]), [])


if __name__ == "__main__":
    unittest.main()
