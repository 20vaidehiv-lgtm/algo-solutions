import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice116.py")


class FirstLetterTwiceTest(unittest.TestCase):
    def test_example(self):
        with patch("builtins.input", return_value="abccbaacz"), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertIn("The first letter to appear twice is: c", buf.getvalue())


if __name__ == "__main__":
    unittest.main()

