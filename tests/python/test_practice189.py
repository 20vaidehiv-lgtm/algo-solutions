import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice189 import Solution  # noqa: E402


class StableMountainsTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.stableMountains([1, 2, 3, 4, 5], 2), [3, 4])
        self.assertEqual(self.sol.stableMountains([10, 1, 10, 1, 10], 3), [1, 3])
        self.assertEqual(self.sol.stableMountains([10, 1, 10, 1, 10], 10), [])


if __name__ == "__main__":
    unittest.main()
