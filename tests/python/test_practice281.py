import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice281 import kangaroo  # noqa: E402


class KangarooTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(kangaroo(0, 3, 4, 2), "YES")
        self.assertEqual(kangaroo(0, 2, 5, 3), "NO")
        self.assertEqual(kangaroo(0, 2, 0, 2), "YES")


if __name__ == "__main__":
    unittest.main()

