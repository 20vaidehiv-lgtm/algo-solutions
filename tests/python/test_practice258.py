import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice258 import Solution  # noqa: E402


class DecompressRLETest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.decompressRLElist([1, 2, 3, 4]), [2, 4, 4, 4])
        self.assertEqual(sol.decompressRLElist([1, 1, 2, 3]), [1, 3, 3])


if __name__ == "__main__":
    unittest.main()

