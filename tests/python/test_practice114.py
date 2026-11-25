import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice114.py")


class CheckAllABeforeBTest(unittest.TestCase):
    def test_true_case(self):
        with patch("builtins.input", return_value="aaabbb"), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertEqual(buf.getvalue().strip(), "True")


if __name__ == "__main__":
    unittest.main()

