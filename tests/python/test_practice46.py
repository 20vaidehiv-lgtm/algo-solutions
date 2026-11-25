# Note: solutions/python/practice46.py is currently unfinished (see header note).
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice46 import Solution  # noqa: E402


class UniqueMorseTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]), 2)
        self.assertEqual(sol.uniqueMorseRepresentations(["a"]), 1)


if __name__ == "__main__":
    unittest.main()

