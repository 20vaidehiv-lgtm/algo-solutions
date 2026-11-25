import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice170.py"
)


class CollectionsCounterTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip()

    def test_sample_purchases(self):
        inputs = [
            "10",
            "2 3 4 5 6 8 7 6 5 18",
            "6",
            "6 55",
            "6 45",
            "6 55",
            "4 40",
            "18 60",
            "10 50",
        ]
        self.assertEqual(self.run_script(inputs), "200")

    def test_no_matching_sizes(self):
        inputs = [
            "3",
            "5 6 7",
            "2",
            "8 100",
            "9 50",
        ]
        self.assertEqual(self.run_script(inputs), "0")


if __name__ == "__main__":
    unittest.main()
