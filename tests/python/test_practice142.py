import io
import os
import runpy
import unittest
from unittest.mock import patch

SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice142.py"
)


class MajorityElementTest(unittest.TestCase):
    def test_majority_found(self):
        with patch("builtins.input", return_value="3 1 3 3 2"), patch(
            "sys.stdout", new_callable=io.StringIO
        ) as stdout:
            with self.assertRaises(SystemExit):
                runpy.run_path(SCRIPT_PATH)
        self.assertEqual(stdout.getvalue().strip(), "3")

    def test_no_majority(self):
        with patch("builtins.input", return_value="1 2 3 4"), patch(
            "sys.stdout", new_callable=io.StringIO
        ) as stdout:
            runpy.run_path(SCRIPT_PATH)
        self.assertEqual(stdout.getvalue().strip(), "-1")


if __name__ == "__main__":
    unittest.main()
