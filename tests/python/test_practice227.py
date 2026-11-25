import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice227 import is_stressful  # noqa: E402


class IsStressfulTest(unittest.TestCase):
    def test_examples_and_rules(self):
        self.assertFalse(is_stressful("Hi"))
        self.assertTrue(is_stressful("I need HELP"))
        self.assertFalse(is_stressful("I neeed HLEP"))
        self.assertTrue(is_stressful("HELP"))
        self.assertTrue(is_stressful("what!!!"))
        self.assertTrue(is_stressful("h-e-l-p"))
        self.assertTrue(is_stressful("uuurrgggeeenttt"))
        self.assertTrue(is_stressful("asap please"))


if __name__ == "__main__":
    unittest.main()
