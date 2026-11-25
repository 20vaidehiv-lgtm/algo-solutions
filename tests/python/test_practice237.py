import io
import os
import runpy
import unittest
from unittest.mock import patch

SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice237.py"
)


class CharacterYearCountMappingTest(unittest.TestCase):
    def test_counts_sorted_ascending(self):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=["3", "Alice", "Bob", "adam"]), patch(
            "sys.stdout", stdout
        ):
            runpy.run_path(SCRIPT_PATH)
        self.assertEqual(stdout.getvalue(), "2006 1\n2005 2\n")

    def test_tail_letters_and_zero_entries(self):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=["2", "sam", "tom"]), patch(
            "sys.stdout", stdout
        ):
            runpy.run_path(SCRIPT_PATH)
        self.assertEqual(stdout.getvalue(), "2003 1\n2004 1\n")

        empty_out = io.StringIO()
        with patch("builtins.input", side_effect=["0"]), patch("sys.stdout", empty_out):
            runpy.run_path(SCRIPT_PATH)
        self.assertEqual(empty_out.getvalue(), "\n")


if __name__ == "__main__":
    unittest.main()
