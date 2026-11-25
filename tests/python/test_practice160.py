import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice160 import Solution, to_linked_list  # noqa: E402


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


class InsertGreatestCommonDivisorsTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(to_list(sol.insertGreatestCommonDivisors(to_linked_list([18, 6, 10, 3]))), [18, 6, 6, 2, 10, 1, 3])
        self.assertEqual(to_list(sol.insertGreatestCommonDivisors(to_linked_list([7]))), [7])


if __name__ == "__main__":
    unittest.main()

