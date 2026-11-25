import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice418 import rank_records  # noqa: E402


class RankRecordsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            rank_records([("Bob", 90), ("Alice", 90), ("Cara", 85)]),
            [(1, "Alice", 90), (2, "Bob", 90), (3, "Cara", 85)],
        )


if __name__ == "__main__":
    unittest.main()

