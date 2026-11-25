import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice41 import Solution, to_list, to_listnode  # noqa: E402


class DeleteDuplicatesTest(unittest.TestCase):
    def test_examples(self):
        sol = Solution()
        self.assertEqual(to_list(sol.deleteDuplicates(to_listnode([1, 1, 2, 3, 3]))), [1, 2, 3])
        self.assertIsNone(sol.deleteDuplicates(None))


if __name__ == "__main__":
    unittest.main()

