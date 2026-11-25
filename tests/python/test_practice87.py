import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice87.py"
)


class EvenDigitCountTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip()

    def test_counts_even_digits(self):
        output = self.run_script(["5", "12 345 2 6 7896"])
        self.assertEqual(output, "Count of integers with an even number of digits: 2")

    def test_no_even_digits(self):
        output = self.run_script(["3", "1 333 55555"])
        self.assertEqual(output, "Count of integers with an even number of digits: 0")


if __name__ == "__main__":
    unittest.main()
