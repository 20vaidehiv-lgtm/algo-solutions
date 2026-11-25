import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice204.py"
)


class WordOrderTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip().splitlines()

    def test_sample(self):
        inputs = ["4", "bcdef", "abcdefg", "bcde", "bcdef"]
        self.assertEqual(self.run_script(inputs), ["3", "2 1 1"])

    def test_all_unique(self):
        inputs = ["3", "alpha", "beta", "gamma"]
        self.assertEqual(self.run_script(inputs), ["3", "1 1 1"])


if __name__ == "__main__":
    unittest.main()
