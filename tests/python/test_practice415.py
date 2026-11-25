import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice415 import character_frequencies  # noqa: E402


class CharacterFrequenciesTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(character_frequencies("aab C"), [("a", 2), ("b", 1), ("c", 1)])
        self.assertEqual(character_frequencies("   "), [])


if __name__ == "__main__":
    unittest.main()

