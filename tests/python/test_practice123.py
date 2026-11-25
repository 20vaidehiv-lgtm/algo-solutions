import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice123.py")


class ThousandDigitFibTest(unittest.TestCase):
    def test_index(self):
        with patch("sys.stdout", new_callable=io.StringIO) as buf:
            ns = runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertEqual(ns["i"], 4782)
        self.assertIn("Index is: 4782", buf.getvalue())


if __name__ == "__main__":
    unittest.main()

