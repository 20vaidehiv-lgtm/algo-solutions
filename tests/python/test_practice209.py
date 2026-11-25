import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice209 import to_weird_case  # noqa: E402


class WeirdStringCaseTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(to_weird_case("This"), "ThIs")
        self.assertEqual(to_weird_case("THIs iS a TEST"), "ThIs Is A TeSt")
        self.assertEqual(to_weird_case("Weird string case"), "WeIrD StRiNg CaSe")


if __name__ == "__main__":
    unittest.main()
