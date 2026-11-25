import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice221 import play_pass  # noqa: E402


class PlayPassTest(unittest.TestCase):
    def test_transformations(self):
        self.assertEqual(play_pass("abc", 1), "AbC")
        self.assertEqual(play_pass("abc def", 1), "AbC EfG")
        self.assertEqual(play_pass("born in 2015!", 1), "BoRn Jo 2015!")
        self.assertEqual(play_pass("z y", 2), "Z A")

    def test_empty(self):
        self.assertEqual(play_pass("", 5), "")


if __name__ == "__main__":
    unittest.main()
