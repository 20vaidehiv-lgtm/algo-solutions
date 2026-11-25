import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice400 import pyramid  # noqa: E402


class PyramidTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(pyramid(1), "/\\\n")
        self.assertEqual(pyramid(2), " /\\\n/__\\\n")
        self.assertEqual(pyramid(3), "  /\\\n /  \\\n/____\\\n")


if __name__ == "__main__":
    unittest.main()

