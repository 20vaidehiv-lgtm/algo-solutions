import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice394 import highest_building  # noqa: E402


class HighestBuildingTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            highest_building([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]),
            [4, 1],
        )
        self.assertEqual(
            highest_building([[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 1]]),
            [3, 4],
        )
        self.assertEqual(
            highest_building([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]),
            [3, 2],
        )

    def test_no_buildings(self):
        self.assertEqual(highest_building([[0, 0], [0, 0]]), [1, 0])


if __name__ == "__main__":
    unittest.main()
