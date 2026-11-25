import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice176.py"
)


class ValidatingCreditCardTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip().splitlines()

    def test_valid_and_invalid_cards(self):
        inputs = [
            "6",
            "4123456789123456",
            "5123-4567-8912-3456",
            "61234-567-8912-3456",
            "4123356789123456",
            "5133-3367-8912-3456",
            "5123 - 3567 - 8912 - 3456",
        ]
        expected = [
            "Valid",
            "Valid",
            "Invalid",
            "Valid",
            "Invalid",
            "Invalid",
        ]
        self.assertEqual(self.run_script(inputs), expected)


if __name__ == "__main__":
    unittest.main()
