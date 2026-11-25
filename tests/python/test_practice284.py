import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice284 import punctuation_score  # noqa: E402


class PunctuationScoreTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(punctuation_score("I like to write multiple sentences. Don't you? Come on!"), 805)
        self.assertEqual(punctuation_score("Hello world!"), 60)


if __name__ == "__main__":
    unittest.main()

