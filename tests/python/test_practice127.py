import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice127 import kth_permutation  # noqa: E402


class KthPermutationTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(kth_permutation(3, 3), '"213"')
        self.assertEqual(kth_permutation(4, 9), '"2314"')
        self.assertEqual(kth_permutation(3, 1), '"123"')

    def test_single_element(self):
        self.assertEqual(kth_permutation(1, 1), '"1"')


if __name__ == "__main__":
    unittest.main()
