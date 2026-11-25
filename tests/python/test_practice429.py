import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice429 import make_list, mergeKLists, to_list  # noqa: E402


class MergeKListsTest(unittest.TestCase):
    def test_examples(self):
        lists = [make_list([1, 4, 5]), make_list([1, 3, 4]), make_list([2, 6])]
        self.assertEqual(to_list(mergeKLists(lists)), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_empty(self):
        self.assertEqual(to_list(mergeKLists([])), [])
        self.assertEqual(to_list(mergeKLists([make_list([])])), [])


if __name__ == "__main__":
    unittest.main()

