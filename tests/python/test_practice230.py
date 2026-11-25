import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice230 import solve  # noqa: E402


class ConsonantValueTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solve("cozy"), 51)
        self.assertEqual(solve("xyzzy"), 126)
        self.assertEqual(solve("zodiac"), 26)
        self.assertEqual(solve("chruschtschov"), 80)
        self.assertEqual(solve("khrushchev"), 38)
        self.assertEqual(solve("strength"), 57)
        self.assertEqual(solve("catchphrase"), 73)
        self.assertEqual(solve("twelfthstreet"), 103)
        self.assertEqual(solve("mischtschenkoana"), 80)

    def test_only_vowels(self):
        self.assertEqual(solve("aeiou"), 0)


if __name__ == "__main__":
    unittest.main()
