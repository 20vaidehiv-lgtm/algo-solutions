import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice101.py"
)


class AlternatingDigitSumTest(unittest.TestCase):
    def run_script(self, n):
        stdout = io.StringIO()
        with patch("builtins.input", return_value=str(n)), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip()

    def test_alternating_digit_sum(self):
        self.assertEqual(self.run_script(521), "Sum: 4")
        self.assertEqual(self.run_script(111), "Sum: 1")
        self.assertEqual(self.run_script(886996), "Sum: 0")


if __name__ == "__main__":
    unittest.main()
