import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice62 import changing_direction  # noqa: E402


class ChangingDirectionTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(changing_direction([1, 2, 3, 4, 5]), 0)
        self.assertEqual(changing_direction([1, 2, 3, 2, 1]), 1)
        self.assertEqual(changing_direction([1, 2, 2, 1, 2, 2]), 2)


if __name__ == "__main__":
    unittest.main()

