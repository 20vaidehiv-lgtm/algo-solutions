import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice216 import good_vs_evil  # noqa: E402


class GoodVsEvilTest(unittest.TestCase):
    def test_outcomes(self):
        self.assertEqual(
            good_vs_evil("1 1 1 1 1 1", "1 1 1 1 1 1 1"),
            "Battle Result: Evil eradicates all trace of Good",
        )
        self.assertEqual(
            good_vs_evil("0 0 0 0 0 10", "0 1 1 1 1 0 0"),
            "Battle Result: Good triumphs over Evil",
        )
        self.assertEqual(
            good_vs_evil("1 0 0 0 0 0", "1 0 0 0 0 0 0"),
            "Battle Result: No victor on this battle field",
        )


if __name__ == "__main__":
    unittest.main()
