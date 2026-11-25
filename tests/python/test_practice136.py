import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice136 import Solution  # noqa: E402


class MaxDistinctTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.maxDistinct("abab"), 2)
        self.assertEqual(self.sol.maxDistinct("abcd"), 4)
        self.assertEqual(self.sol.maxDistinct("aaa"), 1)


if __name__ == "__main__":
    unittest.main()
