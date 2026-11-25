import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice14 import createLinkedList, linkedListToArray, rotateRight  # noqa: E402


class RotateRightTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(linkedListToArray(rotateRight(createLinkedList([1, 2, 3, 4, 5]), 2)), [4, 5, 1, 2, 3])
        self.assertEqual(linkedListToArray(rotateRight(createLinkedList([0, 1, 2]), 4)), [2, 0, 1])

    def test_edge_cases(self):
        self.assertEqual(linkedListToArray(rotateRight(createLinkedList([1, 2]), 1)), [2, 1])
        self.assertEqual(linkedListToArray(rotateRight(createLinkedList([1]), 0)), [1])
        self.assertIsNone(rotateRight(None, 3))


if __name__ == "__main__":
    unittest.main()
