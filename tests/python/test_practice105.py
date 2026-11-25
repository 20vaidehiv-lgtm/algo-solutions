import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice105.py"
)


class ReduceNumberToOneTest(unittest.TestCase):
    def run_script(self, n):
        stdout = io.StringIO()
        with patch("builtins.input", return_value=str(n)), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip()

    def test_min_operations(self):
        self.assertEqual(self.run_script(1), "Minimum number of operations: 0")
        self.assertEqual(self.run_script(8), "Minimum number of operations: 3")
        self.assertEqual(self.run_script(7), "Minimum number of operations: 4")
        self.assertEqual(self.run_script(15), "Minimum number of operations: 5")


if __name__ == "__main__":
    unittest.main()
