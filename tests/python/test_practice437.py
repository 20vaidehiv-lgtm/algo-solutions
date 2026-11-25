import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice437 import common_child  # noqa: E402


class CommonChildTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(common_child("HARRY", "SALLY"), 2)
        self.assertEqual(common_child("AA", "BB"), 0)
        self.assertEqual(common_child("SHINCHAN", "NOHARAAA"), 3)
        self.assertEqual(common_child("ABCDEF", "FBDAMN"), 2)


if __name__ == "__main__":
    unittest.main()

