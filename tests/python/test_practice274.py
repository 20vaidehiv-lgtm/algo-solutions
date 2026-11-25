import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice274 import Solution  # noqa: E402


class UncommonFromSentencesTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(sorted(sol.uncommonFromSentences("this apple is sweet", "this apple is sour")), ["sour", "sweet"])
        self.assertEqual(sol.uncommonFromSentences("apple apple", "banana"), ["banana"])


if __name__ == "__main__":
    unittest.main()

