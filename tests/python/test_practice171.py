import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice171.py"
)


class CompanyLogoTest(unittest.TestCase):
    def run_script(self, s):
        stdout = io.StringIO()
        with patch("builtins.input", return_value=s), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip().splitlines()

    def test_sample(self):
        self.assertEqual(self.run_script("aabbbccde"), ["b 3", "a 2", "c 2"])

    def test_alphabetical_tie_break(self):
        self.assertEqual(self.run_script("cabbca"), ["a 2", "b 2", "c 2"])


if __name__ == "__main__":
    unittest.main()
