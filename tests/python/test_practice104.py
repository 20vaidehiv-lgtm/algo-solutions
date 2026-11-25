import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice104.py"
)


class MultiplyStringsTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip()

    def test_multiply(self):
        self.assertEqual(self.run_script(['"2"', '"3"']), "Product: 6")
        self.assertEqual(self.run_script(["123", "456"]), "Product: 56088")
        self.assertEqual(self.run_script(["0", "999"]), "Product: 0")


if __name__ == "__main__":
    unittest.main()
