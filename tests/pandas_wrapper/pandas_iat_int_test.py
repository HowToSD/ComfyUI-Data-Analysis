import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_iat_int import PandasIatInt

class TestPandasIatInt(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasIatInt()
        self.test_cases = [
            # Test with integer values
            (
                pd.DataFrame({"a": [123]}),
                0, 0,
                (123,)
            ),
            (
                pd.DataFrame({"a": [456]}),
                0, 0,
                (456,)
            ),
            # Test with multiple rows and columns
            (
                pd.DataFrame({
                    "a": [789, 321],
                    "b": [654, 987]
                }),
                1, 1,
                (987,)
            ),
            (
                pd.DataFrame({
                    1: [234],
                    2: [567]
                }),
                0, 1,
                (567,)
            ),
        ]

    def test_select_int_cell(self):
        """Test selecting an integer cell from a pandas DataFrame."""
        for dataframe, row_pos, col_pos, expected in self.test_cases:
            with self.subTest(dataframe=dataframe, row_pos=row_pos, col_pos=col_pos):
                retval = self.node.f(dataframe, row_pos, col_pos)
                self.assertEqual(retval, expected, f"Mismatch for row_pos={row_pos}, col_pos={col_pos}")

if __name__ == "__main__":
    unittest.main()