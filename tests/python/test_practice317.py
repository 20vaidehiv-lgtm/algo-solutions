import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice317 import Solution  # noqa: E402


class FurthestPointFromOriginTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.furthestDistanceFromOrigin("L_RL__R"), 3)
        self.assertEqual(self.sol.furthestDistanceFromOrigin("_R__LL_"), 5)
        self.assertEqual(self.sol.furthestDistanceFromOrigin("_______"), 7)

    def test_balanced(self):
        self.assertEqual(self.sol.furthestDistanceFromOrigin("LR"), 0)


if __name__ == "__main__":
    unittest.main()
