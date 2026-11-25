import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice163.py")


class MatrixScriptTest(unittest.TestCase):
    def test_hackerrank_example(self):
        inputs = ["7 3", "Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "ir!"]
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertEqual(buf.getvalue().strip(), "This is Matrix#  %!")


if __name__ == "__main__":
    unittest.main()

