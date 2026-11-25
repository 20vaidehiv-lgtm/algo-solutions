import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice405.py")


class FloodFillIslandsTest(unittest.TestCase):
    def test_islands_count(self):
        inputs = ["3 3", "110", "010", "001"]
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertEqual(buf.getvalue().strip(), "2")


if __name__ == "__main__":
    unittest.main()

