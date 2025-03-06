import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_iat_set_float import PandasIatSetFloat

class TestPandasIatSetFloat(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasIatSetFloat()
        self.test_cases = [
            # Test with float values
            (
                pd.DataFrame([[None]]),
                0, 0, 3.14
            ),
            (
                pd.DataFrame([[None]]),
                0, 0, 2.71
            ),
            # Test with multiple rows and columns
            (
                pd.DataFrame([[None, None], [None, None]]),
                1, 1, 1.618
            ),
            (
                pd.DataFrame([[None, None]]),
                0, 1, 0.577
            ),
        ]

    def test_set_float_cell(self):
        """Test setting a float cell in a pandas DataFrame."""
        for dataframe, row_pos, col_pos, data in self.test_cases:
            with self.subTest(dataframe=dataframe, row_pos=row_pos, col_pos=col_pos):
                retval = self.node.f(dataframe, row_pos, col_pos, data)
                self.assertEqual(retval[0].iat[row_pos, col_pos],
                                 data, 
                                 f"Mismatch for row_pos={row_pos}, col_pos={col_pos}")

if __name__ == "__main__":
    unittest.main()
