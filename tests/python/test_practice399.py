import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice399 import Solution  # noqa: E402


class FrequencySortTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_examples(self):
        self.assertEqual(
            self.solution.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]),
            [5, -1, 4, 4, -6, -6, 1, 1, 1],
        )
        self.assertEqual(self.solution.frequencySort([1, 1, 2, 2, 2, 3]), [3, 1, 1, 2, 2, 2])
        self.assertEqual(self.solution.frequencySort([2, 3, 1, 3, 2]), [1, 3, 3, 2, 2])

    def test_single_and_empty(self):
        self.assertEqual(self.solution.frequencySort([7]), [7])
        self.assertEqual(self.solution.frequencySort([]), [])


if __name__ == "__main__":
    unittest.main()
