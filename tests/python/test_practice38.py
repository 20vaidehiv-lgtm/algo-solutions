import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice38 import Solution, to_list, to_listnode  # noqa: E402


class MergeTwoSortedListsTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(
            to_list(sol.mergeTwoLists(to_listnode([1, 2, 4]), to_listnode([1, 3, 4]))),
            [1, 1, 2, 3, 4, 4],
        )
        self.assertIsNone(sol.mergeTwoLists(to_listnode([]), to_listnode([])))


if __name__ == "__main__":
    unittest.main()

