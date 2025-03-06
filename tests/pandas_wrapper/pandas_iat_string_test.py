import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_iat_string import PandasIatString

class TestPandasIatString(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasIatString()
        self.test_cases = [
            # Test with string values
            (
                pd.DataFrame({"a": ["hello"]}),
                0, 0,
                ("hello",)
            ),
            (
                pd.DataFrame({"a": ["world"]}),
                0, 0,
                ("world",)
            ),
            # Test with multiple rows and columns
            (
                pd.DataFrame({
                    "a": ["foo", "bar"],
                    "b": ["baz", "qux"]
                }),
                1, 1,
                ("qux",)
            ),
            (
                pd.DataFrame({
                    1: ["alpha"],
                    2: ["beta"]
                }),
                0, 1,
                ("beta",)
            ),
        ]

    def test_select_string_cell(self):
        """Test selecting a string cell from a pandas DataFrame."""
        for dataframe, row_pos, col_pos, expected in self.test_cases:
            with self.subTest(dataframe=dataframe, row_pos=row_pos, col_pos=col_pos):
                retval = self.node.f(dataframe, row_pos, col_pos)
                self.assertEqual(retval, expected, f"Mismatch for row_pos={row_pos}, col_pos={col_pos}")

if __name__ == "__main__":
    unittest.main()
