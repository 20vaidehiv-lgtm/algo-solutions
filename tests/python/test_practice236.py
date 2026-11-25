import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice236 import Solution  # noqa: E402


class ClearDigitsTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(self.solution.clearDigits("abc"), "abc")
        self.assertEqual(self.solution.clearDigits("cb34"), "")
        self.assertEqual(self.solution.clearDigits("1234"), "")

    def test_mixed(self):
        self.assertEqual(self.solution.clearDigits("a1bc2d"), "bd")


if __name__ == "__main__":
    unittest.main()
