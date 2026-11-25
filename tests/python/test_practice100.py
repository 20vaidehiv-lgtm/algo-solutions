import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice100.py"
)


class DoubleReversalTest(unittest.TestCase):
    def run_with_global_n(self, n):
        stdout = io.StringIO()
        with patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, init_globals={"n": n}, run_name="__main__")
        return stdout.getvalue().strip()

    def test_top_level_requires_n(self):
        with self.assertRaises(NameError):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")

    def test_double_reversal_results(self):
        self.assertEqual(self.run_with_global_n(526), "True")
        self.assertEqual(self.run_with_global_n(1800), "False")
        self.assertEqual(self.run_with_global_n(0), "True")


if __name__ == "__main__":
    unittest.main()
