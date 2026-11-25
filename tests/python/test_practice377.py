import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice377 import Solution, list_to_nodes, nodes_to_list  # noqa: E402


class RotateListTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(
            nodes_to_list(self.sol.rotateRight(list_to_nodes([1, 2, 3, 4, 5]), 2)),
            [4, 5, 1, 2, 3],
        )
        self.assertEqual(
            nodes_to_list(self.sol.rotateRight(list_to_nodes([0, 1, 2]), 4)),
            [2, 0, 1],
        )

    def test_single_and_zero_rotation(self):
        self.assertEqual(nodes_to_list(self.sol.rotateRight(list_to_nodes([1]), 5)), [1])
        self.assertEqual(nodes_to_list(self.sol.rotateRight(list_to_nodes([1, 2, 3]), 0)), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
