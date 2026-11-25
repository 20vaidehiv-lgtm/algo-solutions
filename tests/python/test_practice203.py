import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice203 import time_delta  # noqa: E402


class TimeDeltaTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            time_delta("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000"),
            "25200",
        )
        self.assertEqual(
            time_delta("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"),
            "88200",
        )


if __name__ == "__main__":
    unittest.main()
