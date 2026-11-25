import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice96.py"
)


class CountComparisonTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip().splitlines()

    def test_counts(self):
        lines = self.run_script(["5", "8", "1", "2", "2", "3"])
        self.assertEqual(lines[-1], "Results: [0, 4, 2, 2, 1]")

    def test_equal_elements(self):
        lines = self.run_script(["3", "7", "7", "7"])
        self.assertEqual(lines[-1], "Results: [0, 0, 0]")


if __name__ == "__main__":
    unittest.main()
