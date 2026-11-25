import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice113.py")


class RankTransformTest(unittest.TestCase):
    def test_example(self):
        inputs = ["5", "40 10 20 30 10"]
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertIn("Ranks: 4 1 2 3 1", buf.getvalue())


if __name__ == "__main__":
    unittest.main()

