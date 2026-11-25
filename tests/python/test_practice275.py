import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice275 import Solution  # noqa: E402


class CountBinarySubstringsTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.countBinarySubstrings("00110011"), 6)
        self.assertEqual(sol.countBinarySubstrings("10101"), 4)


if __name__ == "__main__":
    unittest.main()

