import os
import sys
import unittest

try:
    import pandas as pd
except ImportError:
    pd = None

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "solutions", "python"))


@unittest.skipIf(pd is None, "pandas is not installed")
class SelectFirstRowsTest(unittest.TestCase):
    def test_examples(self):
        from practice166 import selectFirstRows

        df = pd.DataFrame({"employee_id": [1, 2, 3, 4], "name": ["A", "B", "C", "D"]})
        res = selectFirstRows(df)
        self.assertEqual(len(res), 3)
        self.assertEqual(list(res["employee_id"]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()

