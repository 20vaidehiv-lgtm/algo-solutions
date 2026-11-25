import io
import os
import runpy
import sys
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice308.py"
)


class NotInPlaceScriptTest(unittest.TestCase):
    def test_script_output(self):
        buf = io.StringIO()
        with patch.object(sys, "stdout", buf):
            with self.assertRaises(SystemExit):
                runpy.run_path(SCRIPT_PATH, run_name="__main__")
        self.assertEqual(buf.getvalue().strip(), "E")


if __name__ == "__main__":
    unittest.main()
