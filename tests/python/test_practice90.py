import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice90.py"
)


class ReplaceDigitsTest(unittest.TestCase):
    def run_script(self, s):
        stdout = io.StringIO()
        with patch("builtins.input", return_value=s), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip()

    def test_replace_digits(self):
        self.assertEqual(self.run_script("a1c1e1"), "Transformed string: abcdef")
        self.assertEqual(self.run_script("a1b2c3d4e"), "Transformed string: abbdcfdhe")


if __name__ == "__main__":
    unittest.main()
