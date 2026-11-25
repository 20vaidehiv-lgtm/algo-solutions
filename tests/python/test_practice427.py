import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice427 import Codec, TreeNode  # noqa: E402


class CodecRoundTripTest(unittest.TestCase):
    def test_round_trip_preserves_serialized_form(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        data = Codec().serialize(root)
        self.assertEqual(data, "1,2,3,null,null,4,5,null,null,null,null")
        rebuilt = Codec().deserialize(data)
        self.assertIsNotNone(rebuilt)
        self.assertEqual(Codec().serialize(rebuilt), data)


if __name__ == "__main__":
    unittest.main()
