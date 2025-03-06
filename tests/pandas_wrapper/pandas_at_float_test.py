import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_at_float import PandasAtFloat

class TestPandasAtFloat(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasAtFloat()
        self.test_cases = [
            # Test with float values and string indices
            (
                pd.DataFrame({"a": [123.456]}, index=["row1"]),
                "row1", "string", "a", "string",
                (123.456,)
            ),
            (
                pd.DataFrame({"a": [789.101]}, index=["row2"]),
                "row2", "string", "a", "string",
                (789.101,)
            ),

            # Test with integer indices
            (
                pd.DataFrame({"a": [456.789]}, index=[0]),
                "0", "int", "a", "string",
                (456.789,)
            ),
            (
                pd.DataFrame({"a": [987.654]}, index=[1]),
                "1", "int", "a", "string",
                (987.654,)
            ),

            # Test with integer column labels
            (
                pd.DataFrame({1: [321.654]}, index=[0]),
                "0", "int", 1, "int",
                (321.654,)
            ),
            (
                pd.DataFrame({2: [654.321]}, index=[1]),
                "1", "int", 2, "int",
                (654.321,)
            ),

            # Mixed types: string index, integer column label
            (
                pd.DataFrame({1: [111.222]}, index=["event"]),
                "event", "string", 1, "int",
                (111.222,)
            ),
        ]

    def test_select_float_cell(self):
        """Test selecting a float cell from a pandas DataFrame."""
        for dataframe, row_index, row_index_type, column_label, column_label_type, expected in self.test_cases:
            with self.subTest(dataframe=dataframe, row_index=row_index, column_label=column_label):
                retval = self.node.f(dataframe, row_index, row_index_type, column_label, column_label_type)
                self.assertEqual(retval, expected, f"Mismatch for row_index={row_index}, column_label={column_label}")

if __name__ == "__main__":
    unittest.main()
