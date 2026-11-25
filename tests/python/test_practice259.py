import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice259 import Solution  # noqa: E402


class CountMatchesTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
        self.assertEqual(sol.countMatches(items, "color", "silver"), 1)
        self.assertEqual(sol.countMatches(items, "type", "phone"), 2)


if __name__ == "__main__":
    unittest.main()

