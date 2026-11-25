import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice94.py"
)


class RunningSumTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip().splitlines()

    def test_running_sum(self):
        lines = self.run_script(["4", "1", "2", "3", "4"])
        self.assertEqual(lines[-1], "1 3 6 10")

    def test_with_negatives(self):
        lines = self.run_script(["5", "1", "1", "1", "1", "1"])
        self.assertEqual(lines[-1], "1 2 3 4 5")


if __name__ == "__main__":
    unittest.main()
