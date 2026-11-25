import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice365 import Solution, list_nodes, node_list  # noqa: E402


class DeleteDuplicatesIITest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(
            list_nodes(self.sol.deleteDuplicates(node_list([1, 2, 3, 3, 4, 4, 5]))),
            [1, 2, 5],
        )
        self.assertEqual(
            list_nodes(self.sol.deleteDuplicates(node_list([1, 1, 1, 2, 3]))),
            [2, 3],
        )
        self.assertEqual(
            list_nodes(self.sol.deleteDuplicates(node_list([1, 2, 2]))),
            [1],
        )
        self.assertEqual(
            list_nodes(self.sol.deleteDuplicates(node_list([1, 1, 1]))),
            [],
        )

    def test_empty_and_single(self):
        self.assertIsNone(self.sol.deleteDuplicates(None))
        self.assertEqual(list_nodes(self.sol.deleteDuplicates(node_list([42]))), [42])


if __name__ == "__main__":
    unittest.main()
