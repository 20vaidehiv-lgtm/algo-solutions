import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice98.py"
)


class DaysToWaitLuckierTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip().splitlines()

    def test_daily_temperatures(self):
        lines = self.run_script(["8", "73 74 75 71 69 72 76 73"])
        self.assertEqual(lines[-1], "1 1 4 2 1 1 0 0")

    def test_decreasing(self):
        lines = self.run_script(["3", "30 20 10"])
        self.assertEqual(lines[-1], "0 0 0")


if __name__ == "__main__":
    unittest.main()
