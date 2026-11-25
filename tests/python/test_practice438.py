import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice438 import accum  # noqa: E402


class MumblingTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(accum("abcd"), "A-Bb-Ccc-Dddd")
        self.assertEqual(accum("RqaEzty"), "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy")
        self.assertEqual(accum("cwAt"), "C-Ww-Aaa-Tttt")
        self.assertEqual(accum("Z"), "Z")


if __name__ == "__main__":
    unittest.main()

