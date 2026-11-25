import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice110.py")


class IntersectionTwoArraysTest(unittest.TestCase):
    def test_example(self):
        inputs = ["4", "1 2 2 1", "2", "2 2"]
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertIn("Unique common elements are: 2", buf.getvalue())


if __name__ == "__main__":
    unittest.main()

