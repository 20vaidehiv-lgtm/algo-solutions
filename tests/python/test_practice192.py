import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice192 import ho  # noqa: E402


class HoHoHoTest(unittest.TestCase):
    def test_nested_calls(self):
        self.assertEqual(ho(), "Ho!")
        self.assertEqual(ho(ho()), "Ho Ho!")
        self.assertEqual(ho(ho(ho())), "Ho Ho Ho!")
        self.assertEqual(ho(ho(ho(ho()))), "Ho Ho Ho Ho!")


if __name__ == "__main__":
    unittest.main()
