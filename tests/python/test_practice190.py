import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice190 import Solution  # noqa: E402


class SortPeopleTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(
            self.sol.sortPeople(["Alice", "Bob", "Charlie"], [155, 165, 160]),
            ["Bob", "Charlie", "Alice"],
        )
        self.assertEqual(
            self.sol.sortPeople(["Alice", "Bob", "Bob"], [155, 185, 150]),
            ["Bob", "Alice", "Bob"],
        )


if __name__ == "__main__":
    unittest.main()
