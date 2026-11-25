import os
import sys
import threading
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice329 import Foo  # noqa: E402


class PrintInOrderTest(unittest.TestCase):
    def test_reverse_thread_start(self):
        foo = Foo()
        output = []
        threads = [
            threading.Thread(target=foo.third, args=(lambda: output.append("third"),)),
            threading.Thread(target=foo.second, args=(lambda: output.append("second"),)),
            threading.Thread(target=foo.first, args=(lambda: output.append("first"),)),
        ]
        for t in threads:
            t.start()
        for t in threads:
            t.join(timeout=2)
        self.assertEqual(output, ["first", "second", "third"])

    def test_sequential_order(self):
        foo = Foo()
        output = []
        foo.first(lambda: output.append("first"))
        foo.second(lambda: output.append("second"))
        foo.third(lambda: output.append("third"))
        self.assertEqual(output, ["first", "second", "third"])


if __name__ == "__main__":
    unittest.main()
