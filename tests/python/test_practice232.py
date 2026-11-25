import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice232 import Solution  # noqa: E402


class HammingWeightTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(self.solution.hammingWeight(11), 3)
        self.assertEqual(self.solution.hammingWeight(128), 1)
        self.assertEqual(self.solution.hammingWeight(4294967293), 31)

    def test_zero(self):
        self.assertEqual(self.solution.hammingWeight(0), 0)


if __name__ == "__main__":
    unittest.main()
