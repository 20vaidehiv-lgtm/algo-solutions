import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice301 import viralAdvertising  # noqa: E402


class ViralAdvertisingTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(viralAdvertising(3), 9)
        self.assertEqual(viralAdvertising(4), 15)

    def test_edge_cases(self):
        self.assertEqual(viralAdvertising(0), 0)
        self.assertEqual(viralAdvertising(1), 2)
        self.assertEqual(viralAdvertising(5), 24)


if __name__ == "__main__":
    unittest.main()
