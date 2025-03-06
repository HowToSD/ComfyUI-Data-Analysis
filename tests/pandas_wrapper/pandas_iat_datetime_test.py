import os
import sys
import unittest
import pandas as pd
from datetime import datetime

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_iat_datetime import PandasIatDatetime

class TestPandasIatDatetime(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasIatDatetime()
        self.test_cases = [
            # Test with datetime values
            (
                pd.DataFrame({"a": [datetime(2023, 3, 15, 12, 0, 0)]}),
                0, 0,
                (datetime(2023, 3, 15, 12, 0, 0),)
            ),
            (
                pd.DataFrame({"a": [datetime(2024, 6, 1, 9, 30, 0)]}),
                0, 0,
                (datetime(2024, 6, 1, 9, 30, 0),)
            ),
            # Test with multiple rows and columns
            (
                pd.DataFrame({
                    "a": [datetime(2025, 1, 1, 0, 0, 0), datetime(2022, 12, 31, 23, 59, 59)],
                    "b": [datetime(2020, 2, 29, 14, 15, 16), datetime(2019, 7, 4, 18, 45, 30)]
                }),
                1, 1,
                (datetime(2019, 7, 4, 18, 45, 30),)
            ),
            (
                pd.DataFrame({
                    1: [datetime(2018, 11, 11, 11, 11, 11)],
                    2: [datetime(2017, 5, 23, 6, 30, 0)]
                }),
                0, 1,
                (datetime(2017, 5, 23, 6, 30, 0),)
            ),
        ]

    def test_select_datetime_cell(self):
        """Test selecting a datetime cell from a pandas DataFrame."""
        for dataframe, row_pos, col_pos, expected in self.test_cases:
            with self.subTest(dataframe=dataframe, row_pos=row_pos, col_pos=col_pos):
                retval = self.node.f(dataframe, row_pos, col_pos)
                self.assertEqual(retval, expected, f"Mismatch for row_pos={row_pos}, col_pos={col_pos}")

if __name__ == "__main__":
    unittest.main()
