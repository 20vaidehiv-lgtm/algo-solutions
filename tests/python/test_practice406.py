import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice406.py")


class LongestSubarraySumKTest(unittest.TestCase):
    def test_example(self):
        inputs = ["5 5", "1 2 3 1 1"]
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertEqual(buf.getvalue().strip(), "2")


if __name__ == "__main__":
    unittest.main()

