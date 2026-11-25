import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice13 import getPermutation  # noqa: E402


class GetPermutationTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(getPermutation(3, 3), "213")
        self.assertEqual(getPermutation(4, 9), "2314")
        self.assertEqual(getPermutation(3, 1), "123")

    def test_edge_cases(self):
        self.assertEqual(getPermutation(1, 1), "1")
        self.assertEqual(getPermutation(2, 1), "12")
        self.assertEqual(getPermutation(2, 2), "21")


if __name__ == "__main__":
    unittest.main()
