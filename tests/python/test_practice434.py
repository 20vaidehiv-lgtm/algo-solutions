import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice434 import sun_angle  # noqa: E402


class SunAngleTest(unittest.TestCase):
    def test_daytime(self):
        self.assertEqual(sun_angle("06:00"), 0)
        self.assertEqual(sun_angle("07:00"), 15)
        self.assertEqual(sun_angle("12:15"), 93.75)
        self.assertEqual(sun_angle("18:00"), 180)

    def test_nighttime(self):
        self.assertEqual(sun_angle("01:23"), "I don't see the sun!")
        self.assertEqual(sun_angle("18:01"), "I don't see the sun!")


if __name__ == "__main__":
    unittest.main()

