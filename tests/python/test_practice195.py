import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice195 import bouncing_ball  # noqa: E402


class BouncingBallTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(bouncing_ball(3, 0.66, 1.5), 3)
        self.assertEqual(bouncing_ball(2, 0.5, 1), 1)
        self.assertEqual(bouncing_ball(30, 0.66, 1.5), 15)

    def test_invalid_inputs(self):
        self.assertEqual(bouncing_ball(0, 0.5, 1), -1)
        self.assertEqual(bouncing_ball(3, 1, 1.5), -1)
        self.assertEqual(bouncing_ball(3, 0.5, 3), -1)


if __name__ == "__main__":
    unittest.main()
