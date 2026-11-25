import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice327 import Solution  # noqa: E402


class FindEvenNumbersTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(
            self.sol.findEvenNumbers([2, 1, 3, 0]),
            [102, 120, 130, 132, 210, 230, 302, 310, 312, 320],
        )
        self.assertEqual(
            self.sol.findEvenNumbers([2, 2, 8, 8, 2]),
            [222, 228, 282, 288, 822, 828, 882],
        )
        self.assertEqual(self.sol.findEvenNumbers([3, 7, 5]), [])


if __name__ == "__main__":
    unittest.main()
