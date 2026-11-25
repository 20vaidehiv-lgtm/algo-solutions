import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice391 import top_3_words  # noqa: E402


class Top3WordsTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(
            top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"),
            ["e", "ddd", "aa"],
        )
        self.assertEqual(top_3_words("  //wont won't won't "), ["won't", "wont"])
        self.assertEqual(top_3_words(" ''' , e   .. "), ["e"])

    def test_no_words(self):
        self.assertEqual(top_3_words("  '''  ...  "), [])
        self.assertEqual(top_3_words(""), [])


if __name__ == "__main__":
    unittest.main()
