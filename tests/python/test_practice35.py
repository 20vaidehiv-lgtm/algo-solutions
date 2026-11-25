import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice35 import gradingStudents  # noqa: E402


class GradingStudentsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(gradingStudents([73, 67, 38, 33]), [75, 67, 38, 33])


if __name__ == "__main__":
    unittest.main()

