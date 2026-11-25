import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice9 import lengthOfLastWord  # noqa: E402


class LengthOfLastWordTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(lengthOfLastWord("Hello World"), 5)
        self.assertEqual(lengthOfLastWord("   fly me   to   the moon  "), 4)
        self.assertEqual(lengthOfLastWord("luffy is still joyboy"), 6)

    def test_edge_cases(self):
        self.assertEqual(lengthOfLastWord("a"), 1)
        self.assertEqual(lengthOfLastWord("   a   "), 1)
        self.assertEqual(lengthOfLastWord("   "), 0)


if __name__ == "__main__":
    unittest.main()
