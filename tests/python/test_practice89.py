import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice89.py"
)


class FindWordsContainingCharTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip().splitlines()

    def test_matching_words(self):
        lines = self.run_script(["3", "leet", "code", "abc", "e"])
        self.assertEqual(
            lines,
            [
                "Enter 3 strings:",
                "Strings containing the character 'e'",
                "leet",
                "code",
            ],
        )

    def test_no_matching_words(self):
        lines = self.run_script(["2", "abc", "def", "z"])
        self.assertEqual(
            lines,
            [
                "Enter 2 strings:",
                "Strings containing the character 'z'",
            ],
        )


if __name__ == "__main__":
    unittest.main()
