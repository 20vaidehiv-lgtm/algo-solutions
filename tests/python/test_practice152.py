import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice152 import Solution  # noqa: E402


class DecodeMessageTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(
            sol.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"),
            "this is a secret",
        )


if __name__ == "__main__":
    unittest.main()

