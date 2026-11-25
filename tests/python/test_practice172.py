import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice172.py"
)


class MaximizeItTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip()

    def test_sample(self):
        inputs = [
            "3 1000",
            "2 5 4",
            "3 7 8 9",
            "5 5 7 8 9 10",
        ]
        self.assertEqual(self.run_script(inputs), "206")

    def test_small_modulo(self):
        inputs = [
            "2 10",
            "2 3 4",
            "2 2 5",
        ]
        self.assertEqual(self.run_script(inputs), "9")


if __name__ == "__main__":
    unittest.main()
