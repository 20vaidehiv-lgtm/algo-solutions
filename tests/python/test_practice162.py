import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice162 import Solution  # noqa: E402


class MirrorDistanceTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sol.mirrorDistance(25), 27)
        self.assertEqual(sol.mirrorDistance(121), 0)


if __name__ == "__main__":
    unittest.main()

