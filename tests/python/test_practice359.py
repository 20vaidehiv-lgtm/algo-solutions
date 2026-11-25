import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice359 import alternate  # noqa: E402


class TwoCharactersTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(alternate("asdcbsdcagfsdbgdfanfghbsfdab"), 8)
        self.assertEqual(alternate("asvkugfiugsalddlasguifgukvsa"), 0)
        self.assertEqual(alternate("beabeefeab"), 5)

    def test_single_character_string(self):
        self.assertEqual(alternate("aaaa"), 0)
        self.assertEqual(alternate("abab"), 4)


if __name__ == "__main__":
    unittest.main()
