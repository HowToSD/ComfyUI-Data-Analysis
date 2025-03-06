import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_iat_set_string import PandasIatSetString

class TestPandasIatSetString(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasIatSetString()
        self.test_cases = [
            # Test with string values
            (
                pd.DataFrame([[None]]),
                0, 0, "hello"
            ),
            (
                pd.DataFrame([[None]]),
                0, 0, "world"
            ),
            # Test with multiple rows and columns
            (
                pd.DataFrame([[None, None], [None, None]]),
                1, 1, "foo"
            ),
            (
                pd.DataFrame([[None, None]]),
                0, 1, "bar"
            ),
        ]

    def test_set_string_cell(self):
        """Test setting a string cell in a pandas DataFrame."""
        for dataframe, row_pos, col_pos, data in self.test_cases:
            with self.subTest(dataframe=dataframe, row_pos=row_pos, col_pos=col_pos):
                retval = self.node.f(dataframe, row_pos, col_pos, data)
                self.assertEqual(retval[0].iat[row_pos, col_pos],
                                 data, 
                                 f"Mismatch for row_pos={row_pos}, col_pos={col_pos}")

if __name__ == "__main__":
    unittest.main()
