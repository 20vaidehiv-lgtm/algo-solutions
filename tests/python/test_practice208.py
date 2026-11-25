import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice208 import queue_time  # noqa: E402


class SupermarketQueueTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(queue_time([5, 3, 4], 1), 12)
        self.assertEqual(queue_time([10, 2, 3, 3], 2), 10)
        self.assertEqual(queue_time([2, 3, 10], 2), 12)

    def test_empty_customers(self):
        self.assertEqual(queue_time([], 2), 0)


if __name__ == "__main__":
    unittest.main()
