import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice267 import Solution  # noqa: E402


class NumberComplementTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.findComplement(5), 2)
        self.assertEqual(sol.findComplement(1), 0)


if __name__ == "__main__":
    unittest.main()

