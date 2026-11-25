import io
import os
import runpy
import unittest
from unittest.mock import patch

SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice140.py"
)


class LongestSubarraySumAtMostSTest(unittest.TestCase):
    def test_basic(self):
        inputs = ["5", "1 2 3 4 5", "5"]
        with patch("builtins.input", side_effect=inputs), patch(
            "sys.stdout", new_callable=io.StringIO
        ) as stdout:
            runpy.run_path(SCRIPT_PATH)
        self.assertEqual(stdout.getvalue().strip(), "2")

    def test_replaces_larger_element(self):
        inputs = ["4", "5 1 2 1", "4"]
        with patch("builtins.input", side_effect=inputs), patch(
            "sys.stdout", new_callable=io.StringIO
        ) as stdout:
            runpy.run_path(SCRIPT_PATH)
        self.assertEqual(stdout.getvalue().strip(), "3")


if __name__ == "__main__":
    unittest.main()
