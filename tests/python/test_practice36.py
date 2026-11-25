import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice36 import frequency_sorting  # noqa: E402


class FrequencySortingTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(list(frequency_sorting([1, 2, 3, 4, 5])), [1, 2, 3, 4, 5])
        self.assertEqual(
            list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])),
            [4, 4, 4, 3, 3, 11, 11, 7, 13],
        )


if __name__ == "__main__":
    unittest.main()

