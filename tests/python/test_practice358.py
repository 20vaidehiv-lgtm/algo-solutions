import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice358 import acmTeam  # noqa: E402


class AcmTeamTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            acmTeam(["11101", "10101", "11001", "10111", "10000", "11010", "00010", "01010"]),
            [5, 9],
        )
        self.assertEqual(acmTeam(["10101", "11100", "11010", "00101"]), [5, 2])
        self.assertEqual(acmTeam(["10101", "11110", "00010"]), [5, 1])

    def test_all_zeros(self):
        self.assertEqual(acmTeam(["000", "000", "000"]), [0, 3])


if __name__ == "__main__":
    unittest.main()
