import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice245 import increment_string  # noqa: E402


class StringIncrementerTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(increment_string("foobar001"), "foobar002")
        self.assertEqual(increment_string("foobar00"), "foobar01")
        self.assertEqual(increment_string("foobar99"), "foobar100")
        self.assertEqual(increment_string("foobar099"), "foobar100")
        self.assertEqual(increment_string("fo99obar99"), "fo99obar100")
        self.assertEqual(increment_string(""), "1")
        self.assertEqual(increment_string("foo"), "foo1")


if __name__ == "__main__":
    unittest.main()
