import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice333 import biggerIsGreater  # noqa: E402


class BiggerIsGreaterTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(biggerIsGreater("ab"), "ba")
        self.assertEqual(biggerIsGreater("bb"), "no answer")
        self.assertEqual(biggerIsGreater("hefg"), "hegf")
        self.assertEqual(biggerIsGreater("dkhc"), "hcdk")

    def test_edge_cases(self):
        self.assertEqual(biggerIsGreater("fedcbabcd"), "fedcbabdc")
        self.assertEqual(biggerIsGreater("a"), "no answer")


if __name__ == "__main__":
    unittest.main()
