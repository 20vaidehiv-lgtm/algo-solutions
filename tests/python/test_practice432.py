import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice432 import tower_builder  # noqa: E402


class TowerBuilderTest(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(tower_builder(1), ["*"])
        self.assertEqual(tower_builder(2), [" * ", "***"])
        self.assertEqual(tower_builder(3), ["  *  ", " *** ", "*****"])


if __name__ == "__main__":
    unittest.main()

