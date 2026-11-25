import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice111.py")


class ProductExceptSelfTest(unittest.TestCase):
    def test_example(self):
        inputs = ["4", "1 2 3 4"]
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertIn("24 12 8 6", buf.getvalue())


if __name__ == "__main__":
    unittest.main()

