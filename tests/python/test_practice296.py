import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))

from practice296 import designerPdfViewer  # noqa: E402


class DesignerPdfViewerTest(unittest.TestCase):
    def test_examples(self):
        h1 = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        self.assertEqual(designerPdfViewer(h1, "abc"), 9)

        h2 = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
        self.assertEqual(designerPdfViewer(h2, "zaba"), 28)

    def test_single_letter(self):
        h = [4] * 26
        self.assertEqual(designerPdfViewer(h, "a"), 4)


if __name__ == "__main__":
    unittest.main()
