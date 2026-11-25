import io
import os
import runpy
import unittest
from unittest.mock import patch

SOLUTION_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python", "practice407.py")


class WordLadderTest(unittest.TestCase):
    def test_word_ladder_path(self):
        inputs = ["6", "hot", "dot", "dog", "lot", "log", "cog", "hit", "cog"]
        with patch("builtins.input", side_effect=inputs), patch("sys.stdout", new_callable=io.StringIO):
            ns = runpy.run_path(SOLUTION_PATH, run_name="__main__")
        self.assertEqual(ns["word_ladder"]("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), ["hit", "hot", "dot", "dog", "cog"])


if __name__ == "__main__":
    unittest.main()

