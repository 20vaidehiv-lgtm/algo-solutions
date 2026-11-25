import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice307 import pageCount  # noqa: E402


class PageCountTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(pageCount(5, 3), 1)
        self.assertEqual(pageCount(6, 2), 1)
        self.assertEqual(pageCount(5, 4), 0)

    def test_edge_cases(self):
        self.assertEqual(pageCount(1, 1), 0)
        self.assertEqual(pageCount(6, 5), 1)


if __name__ == "__main__":
    unittest.main()
