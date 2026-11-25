import io
import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice49 import LinkedList  # noqa: E402


class LinkedListTest(unittest.TestCase):
    def test_push_and_print(self):
        ll = LinkedList()
        ll.push(10)
        ll.push(20)
        with patch("sys.stdout", new_callable=io.StringIO) as buf:
            ll.printNodes()
        self.assertEqual(buf.getvalue().strip(), "10 -> 20 -> None")


if __name__ == "__main__":
    unittest.main()

