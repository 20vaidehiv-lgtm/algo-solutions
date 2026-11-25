import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice288 import getMoneySpent  # noqa: E402


class ElectronicsShopTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(getMoneySpent([40, 50, 60], [5, 8, 12], 60), 58)
        self.assertEqual(getMoneySpent([3, 1], [5, 2, 8], 10), 9)
        self.assertEqual(getMoneySpent([4], [5], 5), -1)


if __name__ == "__main__":
    unittest.main()

