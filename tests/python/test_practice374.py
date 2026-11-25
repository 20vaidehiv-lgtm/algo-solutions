import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice374 import add_fracs  # noqa: E402


class AddFractionsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(add_fracs(), "")
        self.assertEqual(add_fracs("1/2", "3/4"), "5/4")
        self.assertEqual(add_fracs("1/2", "1/3", "1/4"), "13/12")

    def test_whole_number_and_single(self):
        self.assertEqual(add_fracs("1/2", "1/2"), "1")
        self.assertEqual(add_fracs("2/3"), "2/3")


if __name__ == "__main__":
    unittest.main()
