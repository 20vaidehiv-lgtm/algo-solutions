import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice85.py"
)


class MaximumAreaLongestDiagonalTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip()

    def test_sample_rectangles(self):
        output = self.run_script(["2", "9 3", "8 6"])
        self.assertEqual(
            output,
            "The area of the rectangle with the longest diagonal is: 48",
        )

    def test_single_rectangle(self):
        output = self.run_script(["1", "3 4"])
        self.assertEqual(
            output,
            "The area of the rectangle with the longest diagonal is: 12",
        )


if __name__ == "__main__":
    unittest.main()
