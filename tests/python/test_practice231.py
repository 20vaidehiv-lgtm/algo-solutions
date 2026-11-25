import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice231 import validate  # noqa: E402


class ValidateCreditCardTest(unittest.TestCase):
    def test_examples(self):
        self.assertTrue(validate(1230))
        self.assertFalse(validate(1714))
        self.assertTrue(validate(2121))
        self.assertFalse(validate(891))
        self.assertTrue(validate(79927398713))


if __name__ == "__main__":
    unittest.main()
