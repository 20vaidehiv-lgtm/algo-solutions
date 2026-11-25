import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice92.py"
)


class AverageExcludingMinMaxTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip().splitlines()

    def test_average_excluding_extremes(self):
        lines = self.run_script(["4", "4000", "3000", "1000", "2000"])
        self.assertEqual(lines[-1], "Average: 2500.00")

    def test_three_elements(self):
        lines = self.run_script(["3", "10", "50", "20"])
        self.assertEqual(lines[-1], "Average: 20.00")


if __name__ == "__main__":
    unittest.main()
