import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice223 import chain  # noqa: E402


class ChainTest(unittest.TestCase):
    def test_chain_functions(self):
        add = lambda x: x + 1
        mul = lambda x: x * 30
        self.assertEqual(chain(2, [add, mul]), 90)
        self.assertEqual(chain(2, [mul, add]), 61)

    def test_empty_functions(self):
        self.assertEqual(chain(5, []), 5)


if __name__ == "__main__":
    unittest.main()
