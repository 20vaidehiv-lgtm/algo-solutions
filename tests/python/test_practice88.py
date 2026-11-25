import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice88.py"
)


class SumMultiplesTest(unittest.TestCase):
    def run_script(self, n):
        stdout = io.StringIO()
        with patch("builtins.input", return_value=str(n)), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip()

    def test_sum_multiples(self):
        self.assertEqual(self.run_script(7), "Sum of all integers: 21")
        self.assertEqual(self.run_script(10), "Sum of all integers: 40")
        self.assertEqual(self.run_script(2), "Sum of all integers: 0")


if __name__ == "__main__":
    unittest.main()
