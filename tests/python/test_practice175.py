import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice175.py"
)


class RegexSubstitutionTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().splitlines()

    def test_replacements(self):
        inputs = [
            "3",
            "a = 1 && b = 2 || c = 3",
            "if a && && b || || c:",
            "x&&y ||z &&w",
        ]
        expected = [
            "a = 1 and b = 2 or c = 3",
            "if a and and b or or c:",
            "x&&y ||z &&w",
        ]
        self.assertEqual(self.run_script(inputs), expected)


if __name__ == "__main__":
    unittest.main()
