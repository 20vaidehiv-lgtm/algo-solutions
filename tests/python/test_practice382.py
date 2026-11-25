import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice382 import camelcase  # noqa: E402


class CamelCaseTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(camelcase("oneTwoThreeFourFiveSixSevenEightNineTen"), 10)
        self.assertEqual(camelcase("saveChangesInTheEditor"), 5)

    def test_edge_cases(self):
        self.assertEqual(camelcase(""), 0)
        self.assertEqual(camelcase("single"), 1)


if __name__ == "__main__":
    unittest.main()
