import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice390 import ips_between  # noqa: E402


class IpsBetweenTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(ips_between("10.11.12.13", "10.11.13.0"), 243)
        self.assertEqual(ips_between("20.0.0.10", "20.0.1.0"), 246)
        self.assertEqual(ips_between("10.0.0.0", "10.0.0.50"), 50)

    def test_same_and_full_range(self):
        self.assertEqual(ips_between("192.168.1.1", "192.168.1.1"), 0)
        self.assertEqual(ips_between("0.0.0.0", "255.255.255.255"), 2**32 - 1)


if __name__ == "__main__":
    unittest.main()
