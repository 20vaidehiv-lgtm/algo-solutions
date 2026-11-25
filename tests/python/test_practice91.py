import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice91.py"
)


class CountPairsTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip().splitlines()

    def test_valid_pairs(self):
        lines = self.run_script(["7", "3", "1", "2", "2", "2", "1", "3", "2"])
        self.assertEqual(lines[-1], "Number of valid pairs: 4")

    def test_no_valid_pairs(self):
        lines = self.run_script(["4", "1", "2", "3", "4", "1"])
        self.assertEqual(lines[-1], "Number of valid pairs: 0")


if __name__ == "__main__":
    unittest.main()
