import io
import os
import runpy
import unittest
from unittest.mock import patch

SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice355.py"
)


class VowelConsonantCounterTest(unittest.TestCase):
    def test_multiple_lines(self):
        inputs = iter(["2", "Hello", "World!"])
        with patch("builtins.input", side_effect=inputs), patch(
            "sys.stdout", new=io.StringIO()
        ) as fake_out:
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        self.assertEqual(fake_out.getvalue(), "2\n3\n3\n7\n21\n")

    def test_single_line_with_punctuation(self):
        inputs = iter(["1", "a1b2 e!"])
        with patch("builtins.input", side_effect=inputs), patch(
            "sys.stdout", new=io.StringIO()
        ) as fake_out:
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        self.assertEqual(fake_out.getvalue(), "2\n1\n2\n")


if __name__ == "__main__":
    unittest.main()
