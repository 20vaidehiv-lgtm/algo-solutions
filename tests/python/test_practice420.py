import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice420 import remove_parentheses  # noqa: E402


class RemoveParenthesesTest(unittest.TestCase):
    def test_basic_and_nested(self):
        self.assertEqual(remove_parentheses("example(unwanted thing)example"), "exampleexample")
        self.assertEqual(remove_parentheses("a(b(c))"), "a")
        self.assertEqual(remove_parentheses("((nested))outside"), "outside")

    def test_edge_cases(self):
        self.assertEqual(remove_parentheses(""), "")
        self.assertEqual(remove_parentheses("plain text"), "plain text")


if __name__ == "__main__":
    unittest.main()

