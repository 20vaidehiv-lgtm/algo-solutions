import io
import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice280 import minion_game  # noqa: E402


class MinionGameTest(unittest.TestCase):
    def test_banana(self):
        with patch("sys.stdout", new_callable=io.StringIO) as buf:
            minion_game("BANANA")
        self.assertEqual(buf.getvalue().strip(), "Stuart 12")


if __name__ == "__main__":
    unittest.main()

