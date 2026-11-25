import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice117.py")


class SmallestEvenMultipleTest(unittest.TestCase):
    def test_example(self):
        with patch("builtins.input", return_value="5"), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertIn("Result: 10", buf.getvalue())


if __name__ == "__main__":
    unittest.main()

