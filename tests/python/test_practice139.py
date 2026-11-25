import io
import os
import runpy
import unittest
from unittest.mock import patch

SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice139.py"
)


class MatrixRotateTest(unittest.TestCase):
    def test_rotate_once(self):
        inputs = ["1 2 3", "4 5 6", "7 8 9", "1"]
        with patch("builtins.input", side_effect=inputs), patch(
            "sys.stdout", new_callable=io.StringIO
        ) as stdout:
            runpy.run_path(SCRIPT_PATH)
        self.assertEqual(stdout.getvalue().strip(), "[7, 4, 1]\n[8, 5, 2]\n[9, 6, 3]")

    def test_rotate_full_circle(self):
        inputs = ["1 2 3", "4 5 6", "7 8 9", "4"]
        with patch("builtins.input", side_effect=inputs), patch(
            "sys.stdout", new_callable=io.StringIO
        ) as stdout:
            runpy.run_path(SCRIPT_PATH)
        self.assertEqual(stdout.getvalue().strip(), "[1, 2, 3]\n[4, 5, 6]\n[7, 8, 9]")


if __name__ == "__main__":
    unittest.main()
