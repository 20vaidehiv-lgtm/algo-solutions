import io
import os
import runpy
import unittest
from unittest.mock import patch


SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "solutions", "python", "practice205.py"
)


class WordsScoreTest(unittest.TestCase):
    def run_script(self, inputs):
        stdout = io.StringIO()
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", stdout):
            ns = runpy.run_path(SCRIPT_PATH, run_name="__main__")
        return stdout.getvalue().strip(), ns

    def test_samples(self):
        out, ns = self.run_script(["2", "hacker book"])
        self.assertEqual(out, "4")
        self.assertEqual(ns["score_words"](["programming", "is", "awesome"]), 4)
        self.assertTrue(ns["is_vowel"]("y"))
        self.assertFalse(ns["is_vowel"]("z"))


if __name__ == "__main__":
    unittest.main()
