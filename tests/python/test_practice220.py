import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice220 import pyramid  # noqa: E402


class PyramidTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(pyramid(0), [])
        self.assertEqual(pyramid(1), [[1]])
        self.assertEqual(pyramid(3), [[1], [1, 1], [1, 1, 1]])
        self.assertEqual(pyramid(4), [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1]])


if __name__ == "__main__":
    unittest.main()
