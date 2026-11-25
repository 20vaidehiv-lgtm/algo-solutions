import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice376 import sortme  # noqa: E402


class SortArrays1Test(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sortme(["one", "two", "three"]), ["one", "three", "two"])

    def test_additional_cases(self):
        self.assertEqual(sortme(["bb", "ba", "aa", "ab"]), ["aa", "ab", "ba", "bb"])
        self.assertEqual(sortme([]), [])


if __name__ == "__main__":
    unittest.main()
