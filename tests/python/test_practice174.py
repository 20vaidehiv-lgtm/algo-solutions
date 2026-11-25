import io
import os
import runpy
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice174 import name_format  # noqa: E402

SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice174.py"
)


class NameDirectoryTest(unittest.TestCase):
    def test_name_format_sorts_by_age(self):
        people = [
            ["Mike", "Thomson", "20", "M"],
            ["Robert", "Bustle", "32", "M"],
            ["Andria", "Bustle", "30", "F"],
        ]
        self.assertEqual(
            name_format(people),
            ["Mr. Mike Thomson", "Ms. Andria Bustle", "Mr. Robert Bustle"],
        )

    def test_script_execution(self):
        inputs = [
            "2",
            "Jane Doe 25 F",
            "John Smith 19 M",
        ]
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            runpy.run_path(SCRIPT_PATH, run_name="__main__")
        self.assertEqual(
            stdout.getvalue().strip().splitlines(),
            ["Mr. John Smith", "Ms. Jane Doe"],
        )


if __name__ == "__main__":
    unittest.main()
