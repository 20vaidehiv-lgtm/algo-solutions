import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice239 import Solution  # noqa: E402


class DecodeXoredArrayTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(self.solution.decode([1, 2, 3], 1), [1, 0, 2, 1])
        self.assertEqual(self.solution.decode([6, 2, 7, 3], 4), [4, 2, 0, 7, 4])

    def test_empty_encoded(self):
        self.assertEqual(self.solution.decode([], 7), [7])


if __name__ == "__main__":
    unittest.main()
