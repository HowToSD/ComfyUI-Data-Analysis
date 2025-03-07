import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_select_column_as_series import PandasSelectColumnAsSeries

class TestPandasSelectColumnAsSeries(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasSelectColumnAsSeries()
        self.test_cases = [
            # Test with a simple DataFrame
            (
                pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}),
                "a",
                pd.Series([1, 2, 3], name="a")
            ),
            # Test with a DataFrame with different data types
            (
                pd.DataFrame({"x": ["foo", "bar"], "y": [10.5, 20.5]}),
                "y",
                pd.Series([10.5, 20.5], name="y")
            ),
            # Test with integer column labels
            (
                pd.DataFrame({1: [100, 200], 2: [300, 400]}),
                1,
                pd.Series([100, 200], name=1)
            ),
            # Test with single-row DataFrame
            (
                pd.DataFrame({"col": [42]}),
                "col",
                pd.Series([42], name="col")
            ),
        ]

    def test_select_column_as_series(self):
        """Test selecting a column as a pandas Series."""
        for df, column_name, expected in self.test_cases:
            with self.subTest(df=df, column_name=column_name):
                retval = self.node.f(df, column_name)
                self.assertIsInstance(retval, tuple, "Return value should be a tuple.")
                self.assertEqual(len(retval), 1, "Return tuple should have a single Series.")
                pd.testing.assert_series_equal(retval[0], expected)

if __name__ == "__main__":
    unittest.main()