import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice69 import string_jump_decoder  # noqa: E402


class StringJumpDecoderTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(string_jump_decoder("a1b2c3"), "abc")
        self.assertEqual(string_jump_decoder(""), "")


if __name__ == "__main__":
    unittest.main()

