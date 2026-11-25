import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice55 import checkio  # noqa: E402


class NonUniqueElementsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(list(checkio([1, 2, 3, 1, 3])), [1, 3, 1, 3])
        self.assertEqual(list(checkio([1, 2, 3, 4, 5])), [])
        self.assertEqual(list(checkio([10, 9, 10, 10, 9, 8])), [10, 9, 10, 10, 9])


if __name__ == "__main__":
    unittest.main()

