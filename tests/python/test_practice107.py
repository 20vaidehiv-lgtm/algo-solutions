import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice107.py")


class BuddyStringsTest(unittest.TestCase):
    def test_false_case(self):
        with patch("builtins.input", side_effect=["ab", "ab"]), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertEqual(buf.getvalue().strip(), "false")


if __name__ == "__main__":
    unittest.main()

