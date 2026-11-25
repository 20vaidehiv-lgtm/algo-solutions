import io
import os
import runpy
import unittest
from unittest.mock import patch

SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice141.py"
)


class GeneratePermutationsTest(unittest.TestCase):
    def test_output(self):
        with patch("sys.stdout", new_callable=io.StringIO) as stdout:
            runpy.run_path(SCRIPT_PATH)
        self.assertEqual(
            stdout.getvalue().strip(),
            "[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]",
        )


if __name__ == "__main__":
    unittest.main()
