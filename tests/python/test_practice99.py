import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice99.py"
)


class HIndexTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip().splitlines()

    def test_h_index(self):
        lines = self.run_script(["5", "3 0 6 1 5"])
        self.assertEqual(lines[-1], "The researcher's h-index is: 3")

    def test_low_citations(self):
        lines = self.run_script(["3", "1 3 1"])
        self.assertEqual(lines[-1], "The researcher's h-index is: 1")


if __name__ == "__main__":
    unittest.main()
