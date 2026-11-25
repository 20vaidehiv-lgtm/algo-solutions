import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice75 import multiplicative_persistence  # noqa: E402


class PersistenceTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(multiplicative_persistence(39), 3)
        self.assertEqual(multiplicative_persistence(999), 4)
        self.assertEqual(multiplicative_persistence(4), 0)


if __name__ == "__main__":
    unittest.main()

