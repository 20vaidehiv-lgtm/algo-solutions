import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice368 import Solution  # noqa: E402


class PeakElementTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        self.assertEqual(self.sol.peakElement([1, 2, 4, 5, 7, 8, 3]), 5)
        self.assertEqual(self.sol.peakElement([1, 2, 3, 4, 5]), 4)
        self.assertEqual(self.sol.peakElement([1, 2]), 1)
        self.assertEqual(self.sol.peakElement([-1]), 0)

    def test_peak_at_start_and_no_peak(self):
        self.assertEqual(self.sol.peakElement([5, 3, 1]), 0)
        self.assertFalse(self.sol.peakElement([2, 2, 2]))


if __name__ == "__main__":
    unittest.main()
