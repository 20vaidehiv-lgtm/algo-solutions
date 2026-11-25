import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice27.py")


class BinaryPalindromeTest(unittest.TestCase):
    def test_non_palindrome(self):
        with patch("builtins.input", return_value="abc"), patch("sys.stdout", new_callable=io.StringIO) as buf:
            runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertEqual(buf.getvalue().strip(), "Not a palindrome")


if __name__ == "__main__":
    unittest.main()

