import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice125 import add_two_numbers, to_list, to_listNode  # noqa: E402


class AddTwoNumbersTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(to_list(add_two_numbers(to_listNode([2, 4, 3]), to_listNode([5, 6, 4]))), [7, 0, 8])
        self.assertEqual(to_list(add_two_numbers(to_listNode([0]), to_listNode([0]))), [0])


if __name__ == "__main__":
    unittest.main()

