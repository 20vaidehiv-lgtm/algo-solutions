import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice37 import Solution, to_list, to_listnode  # noqa: E402


class AddTwoNumbersTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(to_list(sol.addTwoNumbers(to_listnode([2, 4, 3]), to_listnode([5, 6, 4]))), [7, 0, 8])
        self.assertEqual(to_list(sol.addTwoNumbers(to_listnode([9, 9, 9]), to_listnode([1]))), [0, 0, 0, 1])


if __name__ == "__main__":
    unittest.main()

