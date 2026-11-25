import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice278.py")


class CalendarModuleTest(unittest.TestCase):
    def test_example(self):
        with patch("builtins.input", return_value="08 05 2015"), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertEqual(buf.getvalue().strip(), "Wednesday")


if __name__ == "__main__":
    unittest.main()

