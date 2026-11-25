import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice16 import rankTransformArray  # noqa: E402


class RankTransformArrayTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(rankTransformArray([40, 10, 20, 30]), [4, 1, 2, 3])
        self.assertEqual(rankTransformArray([100, 100, 100]), [1, 1, 1])
        self.assertEqual(
            rankTransformArray([37, 12, 28, 9, 100, 56, 80, 5, 12]),
            [5, 3, 4, 2, 8, 6, 7, 1, 3],
        )

    def test_edge_cases(self):
        self.assertEqual(rankTransformArray([]), [])
        self.assertEqual(rankTransformArray([1]), [1])
        self.assertEqual(rankTransformArray([5, 5, 5, 5]), [1, 1, 1, 1])


if __name__ == "__main__":
    unittest.main()
