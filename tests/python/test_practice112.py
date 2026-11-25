import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice112.py")


class CamelCaseWordsTest(unittest.TestCase):
    def test_example(self):
        with patch("builtins.input", return_value="saveChangesInTheEditor"), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertEqual(buf.getvalue().strip().splitlines()[-1], "5")


if __name__ == "__main__":
    unittest.main()

