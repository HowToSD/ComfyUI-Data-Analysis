import os
import sys
import unittest
import pandas as pd
from datetime import datetime

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_iat_set_datetime import PandasIatSetDatetime

class TestPandasIatSetDatetime(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasIatSetDatetime()
        self.test_cases = [
            # Test with datetime values
            (
                pd.DataFrame([[None]]),
                0, 0, datetime(2023, 3, 15, 12, 0, 0)
            ),
            (
                pd.DataFrame([[None]]),
                0, 0, datetime(2024, 6, 1, 9, 30, 0)
            ),
            # Test with multiple rows and columns
            (
                pd.DataFrame([[None, None], [None, None]]),
                1, 1, datetime(2019, 7, 4, 18, 45, 30)
            ),
            (
                pd.DataFrame([[None, None]]),
                0, 1, datetime(2018, 11, 11, 11, 11, 11)
            ),
        ]

    def test_set_datetime_cell(self):
        """Test setting a datetime cell in a pandas DataFrame."""
        for dataframe, row_pos, col_pos, data in self.test_cases:
            with self.subTest(dataframe=dataframe, row_pos=row_pos, col_pos=col_pos):
                retval = self.node.f(dataframe, row_pos, col_pos, data)
                self.assertEqual(retval[0].iat[row_pos, col_pos],
                                 data, 
                                 f"Mismatch for row_pos={row_pos}, col_pos={col_pos}")

if __name__ == "__main__":
    unittest.main()