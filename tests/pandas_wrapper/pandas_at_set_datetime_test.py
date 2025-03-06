import os
import sys
import unittest
import pandas as pd
from datetime import datetime

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_at_set_datetime import PandasAtSetDatetime

class TestPandasAtSetDatetime(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasAtSetDatetime()
        self.test_cases = [
            # Test with string row index and string column label
            (
                pd.DataFrame({"a": [None]}, index=["row1"]),
                "row1", "string", "a", "string", datetime(2023, 3, 15, 12, 0, 0)
            ),
            (
                pd.DataFrame({"a": [None]}, index=["row2"]),
                "row2", "string", "a", "string", datetime(2024, 6, 1, 9, 30, 0)
            ),
            # Test with integer row index and string column label
            (
                pd.DataFrame({"a": [None]}, index=[0]),
                "0", "int", "a", "string", datetime(2025, 1, 1, 0, 0, 0)
            ),
            (
                pd.DataFrame({"a": [None]}, index=[1]),
                "1", "int", "a", "string", datetime(2022, 12, 31, 23, 59, 59)
            ),
            # Test with integer row index and integer column label
            (
                pd.DataFrame({1: [None]}, index=[0]),
                "0", "int", 1, "int", datetime(2020, 2, 29, 14, 15, 16)
            ),
            (
                pd.DataFrame({2: [None]}, index=[1]),
                "1", "int", 2, "int", datetime(2019, 7, 4, 18, 45, 30)
            ),
            # Mixed types: string row index, integer column label
            (
                pd.DataFrame({1: [None]}, index=["event"]),
                "event", "string", 1, "int", datetime(2018, 11, 11, 11, 11, 11)
            ),
        ]

    def test_set_datetime_cell(self):
        """Test setting a datetime cell in a pandas DataFrame."""
        for dataframe, row_index, row_index_type, column_label, column_label_type, data in self.test_cases:
            with self.subTest(dataframe=dataframe, row_index=row_index, column_label=column_label):
                retval = self.node.f(dataframe, row_index, row_index_type, column_label, column_label_type, data)
                self.assertEqual(retval[0].at[int(row_index) if row_index_type == "int" else row_index, 
                                             int(column_label) if column_label_type == "int" else column_label],
                                 data, 
                                 f"Mismatch for row_index={row_index}, column_label={column_label}")

if __name__ == "__main__":
    unittest.main()