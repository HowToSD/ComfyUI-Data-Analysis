import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_at_string import PandasAtString

class TestPandasAtString(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasAtString()
        self.test_cases = [
            # Test with string values and string indices
            (
                pd.DataFrame({"a": ["apple"]}, index=["row1"]),
                "row1", "string", "a", "string",
                ("apple",)
            ),
            (
                pd.DataFrame({"a": ["banana"]}, index=["row2"]),
                "row2", "string", "a", "string",
                ("banana",)
            ),

            # Test with integer indices
            (
                pd.DataFrame({"a": ["cherry"]}, index=[0]),
                "0", "int", "a", "string",
                ("cherry",)
            ),
            (
                pd.DataFrame({"a": ["date"]}, index=[1]),
                "1", "int", "a", "string",
                ("date",)
            ),

            # Test with integer column labels
            (
                pd.DataFrame({1: ["elderberry"]}, index=[0]),
                "0", "int", 1, "int",
                ("elderberry",)
            ),
            (
                pd.DataFrame({2: ["fig"]}, index=[1]),
                "1", "int", 2, "int",
                ("fig",)
            ),

            # Mixed types: string index, integer column label
            (
                pd.DataFrame({1: ["grape"]}, index=["event"]),
                "event", "string", 1, "int",
                ("grape",)
            ),
        ]

    def test_select_string_cell(self):
        """Test selecting a string cell from a pandas DataFrame."""
        for dataframe, row_index, row_index_type, column_label, column_label_type, expected in self.test_cases:
            with self.subTest(dataframe=dataframe, row_index=row_index, column_label=column_label):
                retval = self.node.f(dataframe, row_index, row_index_type, column_label, column_label_type)
                self.assertEqual(retval, expected, f"Mismatch for row_index={row_index}, column_label={column_label}")

if __name__ == "__main__":
    unittest.main()
