import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice387 import correct_polish_letters  # noqa: E402


class CorrectPolishLettersTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(correct_polish_letters("Maria Skłodowska-Curie"), "Maria Sklodowska-Curie")
        self.assertEqual(correct_polish_letters("Jędrzej Błądziński"), "Jedrzej Bladzinski")
        self.assertEqual(correct_polish_letters("Lech Wałęsa"), "Lech Walesa")

    def test_all_diacritics_and_plain(self):
        self.assertEqual(correct_polish_letters("ąćęłńóśźż"), "acelnoszz")
        self.assertEqual(correct_polish_letters("hello"), "hello")


if __name__ == "__main__":
    unittest.main()
