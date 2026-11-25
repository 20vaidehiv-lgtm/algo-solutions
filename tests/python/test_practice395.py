import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice395 import get_cookie  # noqa: E402


class GetCookieTest(unittest.TestCase):
    def test_examples(self):
        cookie = "theme=light; sessionToken=abc123"
        self.assertEqual(get_cookie(cookie, "sessionToken"), "abc123")
        self.assertIsNone(get_cookie(cookie, "userId"))
        self.assertEqual(get_cookie(cookie, "theme"), "light")

    def test_value_with_equals(self):
        self.assertEqual(get_cookie("token=a=b=c; mode=dark", "token"), "a=b=c")


if __name__ == "__main__":
    unittest.main()
