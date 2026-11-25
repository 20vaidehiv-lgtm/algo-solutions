import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice122.py")


class KeypadPhoneTest(unittest.TestCase):
    def test_example(self):
        inputs = ["1", "44 444"]
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertEqual(buf.getvalue().strip(), "hi")


if __name__ == "__main__":
    unittest.main()

