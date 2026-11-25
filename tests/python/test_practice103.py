import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice103.py"
)


class CountUniqueDigitsTest(unittest.TestCase):
    def run_script(self, n):
        stdout = io.StringIO()
        with patch("builtins.input", return_value=str(n)), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip()

    def test_unique_digits_counts(self):
        self.assertEqual(
            self.run_script(1),
            "Count of numbers with unique digits from 0 to 9: 10",
        )
        self.assertEqual(
            self.run_script(2),
            "Count of numbers with unique digits from 0 to 99: 91",
        )


if __name__ == "__main__":
    unittest.main()
