import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice309 import cutTheSticks  # noqa: E402


class CutTheSticksTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(cutTheSticks([5, 4, 4, 2, 2, 8]), [6, 4, 2, 1])
        self.assertEqual(cutTheSticks([1, 2, 3, 4, 3, 3, 2, 1]), [8, 6, 4, 1])

    def test_all_equal(self):
        self.assertEqual(cutTheSticks([3, 3, 3]), [3])


if __name__ == "__main__":
    unittest.main()
