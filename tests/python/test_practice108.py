import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice108.py")


class DominantIndexTest(unittest.TestCase):
    def test_example(self):
        inputs = ["4", "3", "6", "1", "0"]
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertIn("Dominant Index: 1", buf.getvalue())


if __name__ == "__main__":
    unittest.main()

