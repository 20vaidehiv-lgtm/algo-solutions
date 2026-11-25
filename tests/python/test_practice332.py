import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice332 import jumpingOnClouds  # noqa: E402


class JumpingOnCloudsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]), 4)
        self.assertEqual(jumpingOnClouds([0, 0, 0, 1, 0, 0]), 3)
        self.assertEqual(jumpingOnClouds([0, 0, 0, 0, 1, 0]), 3)

    def test_minimal(self):
        self.assertEqual(jumpingOnClouds([0, 0]), 1)


if __name__ == "__main__":
    unittest.main()
