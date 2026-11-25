import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice289 import angryProfessor  # noqa: E402


class AngryProfessorTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(angryProfessor(3, [-1, -3, 4, 2]), "YES")
        self.assertEqual(angryProfessor(2, [0, -1, 2, 1]), "NO")


if __name__ == "__main__":
    unittest.main()

