import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice304 import Solution  # noqa: E402


class SortSentenceTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.sortSentence("is2 sentence4 This1 a3"), "This is a sentence")
        self.assertEqual(self.sol.sortSentence("Myself2 Me1 I4 and3"), "Me Myself and I")

    def test_single_word(self):
        self.assertEqual(self.sol.sortSentence("word1"), "word")


if __name__ == "__main__":
    unittest.main()
