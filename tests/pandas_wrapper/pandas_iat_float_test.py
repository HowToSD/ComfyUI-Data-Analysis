import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_iat_float import PandasIatFloat

class TestPandasIatFloat(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasIatFloat()
        self.test_cases = [
            # Test with float values
            (
                pd.DataFrame({"a": [1.23]}),
                0, 0,
                (1.23,)
            ),
            (
                pd.DataFrame({"a": [4.56]}),
                0, 0,
                (4.56,)
            ),
            # Test with multiple rows and columns
            (
                pd.DataFrame({
                    "a": [7.89, 3.21],
                    "b": [6.54, 9.87]
                }),
                1, 1,
                (9.87,)
            ),
            (
                pd.DataFrame({
                    1: [2.34],
                    2: [5.67]
                }),
                0, 1,
                (5.67,)
            ),
        ]

    def test_select_float_cell(self):
        """Test selecting a float cell from a pandas DataFrame."""
        for dataframe, row_pos, col_pos, expected in self.test_cases:
            with self.subTest(dataframe=dataframe, row_pos=row_pos, col_pos=col_pos):
                retval = self.node.f(dataframe, row_pos, col_pos)
                self.assertEqual(retval, expected, f"Mismatch for row_pos={row_pos}, col_pos={col_pos}")

if __name__ == "__main__":
    unittest.main()
