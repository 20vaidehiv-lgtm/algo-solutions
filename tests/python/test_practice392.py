import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice392 import to_underscore  # noqa: E402


class ToUnderscoreTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(to_underscore("MoviesAndBooks"), "movies_and_books")
        self.assertEqual(to_underscore("TestController"), "test_controller")
        self.assertEqual(to_underscore("App7Test"), "app7_test")

    def test_numeric_and_empty(self):
        self.assertEqual(to_underscore(1), "1")
        self.assertEqual(to_underscore(""), "")


if __name__ == "__main__":
    unittest.main()
