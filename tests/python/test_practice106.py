import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice106.py")


class BackspaceStringCompareTest(unittest.TestCase):
    def test_match(self):
        with patch("builtins.input", side_effect=["ab#c", "ac"]), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertEqual(buf.getvalue().strip(), "true")


if __name__ == "__main__":
    unittest.main()

