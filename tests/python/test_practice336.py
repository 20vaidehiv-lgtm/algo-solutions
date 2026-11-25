import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice336 import Solution  # noqa: E402


class HappyNumberTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertTrue(self.sol.isHappy(19))
        self.assertFalse(self.sol.isHappy(2))
        self.assertTrue(self.sol.isHappy(7))

    def test_one(self):
        self.assertTrue(self.sol.isHappy(1))


if __name__ == "__main__":
    unittest.main()
