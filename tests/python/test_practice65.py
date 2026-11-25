import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice65 import frequency_counter  # noqa: E402


class FrequencyCounterTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(frequency_counter(["a", "b", "a", "c", "b", "a"]), "a - 3, b - 2, c - 1")
        self.assertEqual(frequency_counter([]), "")


if __name__ == "__main__":
    unittest.main()

