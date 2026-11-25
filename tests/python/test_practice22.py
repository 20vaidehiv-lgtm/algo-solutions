import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice22.py")


class PascalTriangleTest(unittest.TestCase):
    def test_four_rows(self):
        with patch("builtins.input", return_value="4"), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        lines = [line.strip() for line in buf.getvalue().strip().splitlines()]
        self.assertEqual(lines, ["1", "1 1", "1 2 1", "1 3 3 1"])


if __name__ == "__main__":
    unittest.main()

