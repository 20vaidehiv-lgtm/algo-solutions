import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice28 import reverseN, reverseNOptimized  # noqa: E402


class ReverseIntegerTest(unittest.TestCase):
    def test_examples(self):
        for fn in (reverseN, reverseNOptimized):
            self.assertEqual(fn(123), 321)
            self.assertEqual(fn(-123), -321)
            self.assertEqual(fn(120), 21)
            self.assertEqual(fn(0), 0)

    def test_overflow(self):
        self.assertEqual(reverseNOptimized(1534236469), 0)


if __name__ == "__main__":
    unittest.main()

