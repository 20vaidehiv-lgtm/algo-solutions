import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice79 import print_character_triangle  # noqa: E402


class CharacterTriangleTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(print_character_triangle("*", 3), " *\n***\n*****")
        self.assertEqual(print_character_triangle("#", 1), "#")
        self.assertEqual(print_character_triangle("*", 0), "")


if __name__ == "__main__":
    unittest.main()

