import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice219 import highest_rank  # noqa: E402


class HighestRankTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(highest_rank([1, 2, 3, 2, 1, 3, 3]), 3)
        self.assertEqual(highest_rank([1, 1, 2, 2, 3]), 2)
        self.assertEqual(highest_rank([1, 2, 3, 4, 5]), 5)

    def test_single_element(self):
        self.assertEqual(highest_rank([42]), 42)


if __name__ == "__main__":
    unittest.main()
