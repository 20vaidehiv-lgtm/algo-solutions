import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice270 import meeting  # noqa: E402


class MeetingTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull"),
            "(CORWILL, FRED)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)",
        )


if __name__ == "__main__":
    unittest.main()

