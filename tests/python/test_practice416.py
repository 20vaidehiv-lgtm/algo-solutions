import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice416 import second_largest  # noqa: E402


class SecondLargestTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(second_largest([10, 20, 20, 30]), 20)
        self.assertEqual(second_largest([5, 5, 5, 4]), 4)


if __name__ == "__main__":
    unittest.main()

