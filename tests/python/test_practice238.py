import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice238 import count_words  # noqa: E402


class MonkeyTypingTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}), 2)
        self.assertEqual(
            count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}),
            3,
        )
        self.assertEqual(
            count_words("Lorem ipsum dolor sit amet", {"sum", "hamlet", "infinity", "anything"}),
            1,
        )


if __name__ == "__main__":
    unittest.main()
