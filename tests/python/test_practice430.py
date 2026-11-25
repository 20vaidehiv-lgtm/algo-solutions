import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice430 import icecream_parlor  # noqa: E402


class IceCreamParlorTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(icecream_parlor(4, [1, 4, 5, 3, 2]), [1, 4])
        self.assertEqual(icecream_parlor(4, [2, 2, 4, 3]), [1, 2])
        self.assertEqual(icecream_parlor(9, [1, 3, 4, 6, 7, 9]), [2, 4])
        self.assertEqual(icecream_parlor(8, [2, 1, 9, 4, 4, 56, 90, 3]), [4, 5])


if __name__ == "__main__":
    unittest.main()

