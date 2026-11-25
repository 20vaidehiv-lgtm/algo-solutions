import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice93.py"
)


class MinOpsDivisibleByThreeTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip().splitlines()

    def test_operations(self):
        lines = self.run_script(["4", "1", "2", "3", "4"])
        self.assertEqual(lines[-1], "Minimum number of operation: 3")

    def test_already_divisible(self):
        lines = self.run_script(["3", "3", "6", "9"])
        self.assertEqual(lines[-1], "Minimum number of operation: 0")


if __name__ == "__main__":
    unittest.main()
