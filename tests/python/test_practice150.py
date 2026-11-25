import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice150 import Solution  # noqa: E402


class CountAsterisksTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.countAsterisks("l|*e*et|c**o|*de|"), 2)
        self.assertEqual(sol.countAsterisks("iamprogrammer"), 0)
        self.assertEqual(sol.countAsterisks("yo|uar|e**|b|e***au|tifu|l"), 5)


if __name__ == "__main__":
    unittest.main()

