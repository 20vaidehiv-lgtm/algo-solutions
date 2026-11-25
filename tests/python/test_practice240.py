import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice240 import ParkingSystem  # noqa: E402


class ParkingSystemTest(unittest.TestCase):
    def test_add_car(self):
        parking = ParkingSystem(1, 1, 0)
        self.assertTrue(parking.addCar(1))
        self.assertTrue(parking.addCar(2))
        self.assertFalse(parking.addCar(3))
        self.assertFalse(parking.addCar(1))
        self.assertFalse(parking.addCar(2))


if __name__ == "__main__":
    unittest.main()
