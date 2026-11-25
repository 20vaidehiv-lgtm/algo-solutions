import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice306 import Solution  # noqa: E402


class FindMissingElementsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.findMissingElements([1, 4, 2, 5]), [3])
        self.assertEqual(self.sol.findMissingElements([5, 1]), [2, 3, 4])

    def test_edge_cases(self):
        self.assertEqual(self.sol.findMissingElements([1, 2, 3]), [])
        self.assertEqual(self.sol.findMissingElements([7]), [])


if __name__ == "__main__":
    unittest.main()
