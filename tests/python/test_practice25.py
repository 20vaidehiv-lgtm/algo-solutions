import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice25.py")


class SumOfOnesTest(unittest.TestCase):
    def test_output(self):
        with patch("sys.stdout", new_callable=io.StringIO) as buf:
            ns = runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertEqual(int(buf.getvalue().strip()), ns["result"])
        self.assertGreater(ns["result"], 0)


if __name__ == "__main__":
    unittest.main()

