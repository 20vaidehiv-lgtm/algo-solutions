import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice402 import permutations  # noqa: E402


class PermutationsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sorted(permutations("a")), ["a"])
        self.assertEqual(
            sorted(permutations("aabb")),
            ["aabb", "abab", "abba", "baab", "baba", "bbaa"],
        )
        self.assertEqual(len(permutations("abcd")), 24)


if __name__ == "__main__":
    unittest.main()

