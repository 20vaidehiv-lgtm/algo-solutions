import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice426 import can_finish  # noqa: E402


class CourseScheduleTest(unittest.TestCase):
    def test_possible(self):
        self.assertTrue(can_finish(2, [[1, 0]]))
        self.assertTrue(can_finish(5, [[1, 0], [2, 1], [3, 2], [4, 3]]))
        self.assertTrue(can_finish(1, []))

    def test_cycles(self):
        self.assertFalse(can_finish(2, [[1, 0], [0, 1]]))
        self.assertFalse(can_finish(3, [[0, 1], [1, 2], [2, 0]]))


if __name__ == "__main__":
    unittest.main()

