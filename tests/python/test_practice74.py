import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice74 import nearest_value  # noqa: E402


class NearestValueTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(nearest_value({17, 4, 7, 10, 11, 12}, 9), 10)
        self.assertEqual(nearest_value({17, 4, 7, 10, 11, 12}, 8), 7)
        self.assertEqual(nearest_value({5}, 7), 5)


if __name__ == "__main__":
    unittest.main()

