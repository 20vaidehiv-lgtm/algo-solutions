import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice187 import Solution  # noqa: E402


class MostWordsFoundTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(
            self.sol.mostWordsFound(
                ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
            ),
            6,
        )
        self.assertEqual(
            self.sol.mostWordsFound(["please wait", "continue to fight", "continue to win"]),
            3,
        )


if __name__ == "__main__":
    unittest.main()
