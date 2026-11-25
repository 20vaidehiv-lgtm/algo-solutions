import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice95.py"
)


class StepsToZeroTest(unittest.TestCase):
    def run_script(self, n):
        stdout = io.StringIO()
        with patch("builtins.input", return_value=str(n)), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip()

    def test_steps_to_zero(self):
        self.assertEqual(self.run_script(14), "Number of steps to reduce N to 0: 6")
        self.assertEqual(self.run_script(8), "Number of steps to reduce N to 0: 4")
        self.assertEqual(self.run_script(0), "Number of steps to reduce N to 0: 0")


if __name__ == "__main__":
    unittest.main()
