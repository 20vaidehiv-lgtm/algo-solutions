import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice167 import Solution  # noqa: E402


class XorOperationTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.xorOperation(5, 0), 8)
        self.assertEqual(sol.xorOperation(4, 3), 8)


if __name__ == "__main__":
    unittest.main()

