import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice207 import wave  # noqa: E402


class MexicanWaveTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(wave("hello"), ["Hello", "hEllo", "heLlo", "helLo", "hellO"])
        self.assertEqual(wave("gap"), ["Gap", "gAp", "gaP"])
        self.assertEqual(
            wave("two words"),
            [
                "Two words",
                "tWo words",
                "twO words",
                "two Words",
                "two wOrds",
                "two woRds",
                "two worDs",
                "two wordS",
            ],
        )

    def test_empty(self):
        self.assertEqual(wave(""), [])


if __name__ == "__main__":
    unittest.main()
