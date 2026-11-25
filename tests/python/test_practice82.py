import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice82 import myPow  # noqa: E402


class MyPowTest(unittest.TestCase):
    def test_examples(self):
        self.assertAlmostEqual(myPow(2.0, 10), 1024.0, places=5)
        self.assertAlmostEqual(myPow(2.0, -2), 0.25, places=5)
        self.assertAlmostEqual(myPow(2.0, 0), 1.0, places=5)


if __name__ == "__main__":
    unittest.main()

