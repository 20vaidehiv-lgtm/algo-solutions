import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice389 import next_bigger  # noqa: E402


class NextBiggerTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(next_bigger(2017), 2071)
        self.assertEqual(next_bigger(144), 414)
        self.assertEqual(next_bigger(12), 21)

    def test_no_bigger_permutation(self):
        self.assertEqual(next_bigger(9), -1)
        self.assertEqual(next_bigger(111), -1)
        self.assertEqual(next_bigger(531), -1)


if __name__ == "__main__":
    unittest.main()
