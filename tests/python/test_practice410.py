import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice410 import speedify  # noqa: E402


class SpeedifyTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(speedify("AZ"), "A                         Z")
        self.assertEqual(speedify("ABC"), "A B C")
        self.assertEqual(speedify("ACE"), "A  C  E")
        self.assertEqual(speedify("CBA"), "  A")
        self.assertEqual(speedify("HELLOWORLD"), "     E H    DLL   OLO   R  W")


if __name__ == "__main__":
    unittest.main()

