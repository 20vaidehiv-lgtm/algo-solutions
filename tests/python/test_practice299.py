import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice299 import permutationEquation  # noqa: E402


class PermutationEquationTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(permutationEquation([5, 2, 1, 3, 4]), [4, 2, 5, 1, 3])
        self.assertEqual(permutationEquation([4, 3, 5, 1, 2]), [1, 3, 5, 4, 2])
        self.assertEqual(permutationEquation([2, 3, 1]), [2, 3, 1])

    def test_single_element(self):
        self.assertEqual(permutationEquation([1]), [1])


if __name__ == "__main__":
    unittest.main()
