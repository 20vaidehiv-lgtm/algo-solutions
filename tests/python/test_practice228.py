import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice228 import lost_moons  # noqa: E402


class LostMoonsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            lost_moons(["Earth", "Mars", "Jupiter"], ["Moon", "Phobos", "Europa"]),
            [["Earth", "Moon"], ["Mars", "Phobos"], ["Jupiter", "Europa"]],
        )
        self.assertEqual(
            lost_moons(["Earth", "Mars", "Jupiter"], ["Deimos", "Ganymede", "Io"]),
            [["Earth"], ["Mars", "Deimos"], ["Io", "Jupiter", "Ganymede"]],
        )
        self.assertEqual(
            lost_moons(["Earth", "Mars", "Jupiter"], ["Callisto", "Dione", "Iapetus"]),
            [["Earth"], ["Mars"], ["Jupiter", "Callisto"]],
        )

    def test_planet_ordering(self):
        self.assertEqual(
            lost_moons(["Mars", "Mercury"], ["Deimos", "Phobos"]),
            [["Mercury"], ["Phobos", "Mars", "Deimos"]],
        )


if __name__ == "__main__":
    unittest.main()
