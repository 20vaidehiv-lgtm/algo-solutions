import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice344 import Solution  # noqa: E402


class KthLargestTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.kthLargest([1, 2, 3, 4, 5], 2), [-1, 1, 2, 3, 4])
        self.assertEqual(self.sol.kthLargest([1, 2, 3, 4, 5], 3), [-1, -1, 1, 2, 3])
        self.assertEqual(self.sol.kthLargest([1, 2, 3, 4, 5], 4), [-1, -1, -1, 1, 2])

    def test_unsorted_and_k1(self):
        self.assertEqual(self.sol.kthLargest([10, 20, 11, 70, 50], 3), [-1, -1, 10, 11, 20])
        self.assertEqual(self.sol.kthLargest([3, 1, 5], 1), [3, 3, 5])


if __name__ == "__main__":
    unittest.main()
