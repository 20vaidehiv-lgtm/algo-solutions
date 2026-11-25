import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice184 import Solution  # noqa: E402


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RangeSumBSTTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example(self):
        root = TreeNode(
            10,
            TreeNode(5, TreeNode(3), TreeNode(7)),
            TreeNode(15, None, TreeNode(18)),
        )
        self.assertEqual(self.sol.rangeSumBST(root, 7, 15), 32)

    def test_single_node(self):
        root = TreeNode(10)
        self.assertEqual(self.sol.rangeSumBST(root, 5, 15), 10)
        self.assertEqual(self.sol.rangeSumBST(root, 1, 5), 0)


if __name__ == "__main__":
    unittest.main()
