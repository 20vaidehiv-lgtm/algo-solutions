import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice256 import word_ladder  # noqa: E402


class WordLadderTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5)
        self.assertEqual(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)


if __name__ == "__main__":
    unittest.main()

