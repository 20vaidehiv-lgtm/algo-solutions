import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice285 import birthday  # noqa: E402


class BirthdayTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(birthday([1, 2, 1, 3, 2], 3, 2), 2)
        self.assertEqual(birthday([4], 4, 1), 1)


if __name__ == "__main__":
    unittest.main()

