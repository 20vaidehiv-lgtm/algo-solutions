import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice215 import title_case  # noqa: E402


class TitleCaseTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(title_case("a clash of KINGS", "a an the of"), "A Clash of Kings")
        self.assertEqual(title_case("THE WIND IN THE WILLOWS", "The In"), "The Wind in the Willows")
        self.assertEqual(title_case("the quick brown fox"), "The Quick Brown Fox")

    def test_empty_and_first_minor(self):
        self.assertEqual(title_case(""), "")
        self.assertEqual(title_case("the of the", "the of"), "The of the")


if __name__ == "__main__":
    unittest.main()
