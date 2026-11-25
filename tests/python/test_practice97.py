import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice97.py"
)


class BeautifulDaysTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip()

    def test_beautiful_days_range(self):
        output = self.run_script(["20", "24", "6"])
        self.assertEqual(output, "The number of just right number is: 2")

    def test_single_day_match(self):
        output = self.run_script(["12", "13", "9"])
        self.assertEqual(output, "The number of just right number is: 1")


if __name__ == "__main__":
    unittest.main()
