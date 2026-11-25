import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice179 import Solution  # noqa: E402


class TruncateSentenceTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(
            self.sol.truncateSentence("Hello how are you Contestant", 4),
            "Hello how are you",
        )
        self.assertEqual(
            self.sol.truncateSentence("What is the solution to this problem", 4),
            "What is the solution",
        )

    def test_all_words(self):
        self.assertEqual(self.sol.truncateSentence("chopper is not a tanuki", 5), "chopper is not a tanuki")


if __name__ == "__main__":
    unittest.main()
