import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice383 import runningTime  # noqa: E402


class RunningTimeTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(runningTime([8, 6, 6, 42, 8, 1, 1, 13, 4, 6, 2, 1, 1, 39]), 51)
        self.assertEqual(runningTime([2, 1, 3, 1, 2]), 4)
        self.assertEqual(runningTime([1, 1, 1, 2, 2]), 0)

    def test_edge_cases(self):
        self.assertEqual(runningTime([]), 0)
        self.assertEqual(runningTime([5]), 0)
        self.assertEqual(runningTime([3, 2, 1]), 3)


if __name__ == "__main__":
    unittest.main()
