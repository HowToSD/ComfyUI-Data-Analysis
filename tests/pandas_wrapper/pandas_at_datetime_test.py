import os
import sys
import unittest
import pandas as pd
from datetime import datetime

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_at_datetime import PandasAtDatetime

class TestPandasAtDatetime(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasAtDatetime()
        self.test_cases = [
            # Test with datetime values and string indices
            (
                pd.DataFrame({"a": [datetime(2023, 3, 15, 12, 0, 0)]}, index=["row1"]),
                "row1", "string", "a", "string",
                (datetime(2023, 3, 15, 12, 0, 0),)
            ),
            (
                pd.DataFrame({"a": [datetime(2024, 6, 1, 9, 30, 0)]}, index=["row2"]),
                "row2", "string", "a", "string",
                (datetime(2024, 6, 1, 9, 30, 0),)
            ),

            # Test with integer indices
            (
                pd.DataFrame({"a": [datetime(2025, 1, 1, 0, 0, 0)]}, index=[0]),
                "0", "int", "a", "string",
                (datetime(2025, 1, 1, 0, 0, 0),)
            ),
            (
                pd.DataFrame({"a": [datetime(2022, 12, 31, 23, 59, 59)]}, index=[1]),
                "1", "int", "a", "string",
                (datetime(2022, 12, 31, 23, 59, 59),)
            ),

            # Test with integer column labels
            (
                pd.DataFrame({1: [datetime(2020, 2, 29, 14, 15, 16)]}, index=[0]),
                "0", "int", 1, "int",
                (datetime(2020, 2, 29, 14, 15, 16),)
            ),
            (
                pd.DataFrame({2: [datetime(2019, 7, 4, 18, 45, 30)]}, index=[1]),
                "1", "int", 2, "int",
                (datetime(2019, 7, 4, 18, 45, 30),)
            ),

            # Mixed types: string index, integer column label
            (
                pd.DataFrame({1: [datetime(2018, 11, 11, 11, 11, 11)]}, index=["event"]),
                "event", "string", 1, "int",
                (datetime(2018, 11, 11, 11, 11, 11),)
            ),
        ]

    def test_select_datetime_cell(self):
        """Test selecting a datetime cell from a pandas DataFrame."""
        for dataframe, row_index, row_index_type, column_label, column_label_type, expected in self.test_cases:
            with self.subTest(dataframe=dataframe, row_index=row_index, column_label=column_label):
                retval = self.node.f(dataframe, row_index, row_index_type, column_label, column_label_type)
                self.assertEqual(retval, expected, f"Mismatch for row_index={row_index}, column_label={column_label}")

if __name__ == "__main__":
    unittest.main()
