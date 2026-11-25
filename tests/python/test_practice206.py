import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice206.py"
)


class CompressStringTest(unittest.TestCase):
    def run_script(self, s):
        stdout = io.StringIO()
        with patch("builtins.input", return_value=s), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip()

    def test_sample(self):
        self.assertEqual(self.run_script("1222311"), "(1, 1) (3, 2) (1, 3) (2, 1)")

    def test_single_digit(self):
        self.assertEqual(self.run_script("5"), "(1, 5)")


if __name__ == "__main__":
    unittest.main()
