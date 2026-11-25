import io
import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice348 import Solution  # noqa: E402


class PrintNosTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_examples(self):
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            res = self.sol.printNos(10)
            self.assertIsNone(res)
            self.assertEqual(fake_out.getvalue(), "10 9 8 7 6 5 4 3 2 1 ")

        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            self.sol.printNos(5)
            self.assertEqual(fake_out.getvalue(), "5 4 3 2 1 ")

        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            self.sol.printNos(2)
            self.assertEqual(fake_out.getvalue(), "2 1 ")

    def test_zero(self):
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            self.sol.printNos(0)
            self.assertEqual(fake_out.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
