import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_boolean_index import PandasBooleanIndex

class TestPandasBooleanIndex(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasBooleanIndex()
        self.valid_test_cases = [
            # Basic boolean indexing
            (
                pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, index=["x", "y", "z"]),
                pd.Series([True, False, True], index=["x", "y", "z"]),
                pd.DataFrame({"a": [1, 3], "b": [4, 6]}, index=["x", "z"])
            ),
            # All True case
            (
                pd.DataFrame({"a": [10, 20, 30]}),
                pd.Series([True, True, True]),
                pd.DataFrame({"a": [10, 20, 30]})
            ),
            # All False case
            (
                pd.DataFrame({"a": [100, 200, 300]}),
                pd.Series([False, False, False]),
                pd.DataFrame({"a": []}).astype("int64")
            ),
            # Mixed True/False with different index labels
            (
                pd.DataFrame({"a": [1.1, 2.2, 3.3]}, index=["row1", "row2", "row3"]),
                pd.Series([False, True, False], index=["row1", "row2", "row3"]),
                pd.DataFrame({"a": [2.2]}, index=["row2"])
            ),
        ]

        self.invalid_test_cases = [
            # Series with incorrect index
            (
                pd.DataFrame({"a": [1, 2, 3]}, index=["x", "y", "z"]),
                pd.Series([True, False], index=["x", "y"]),  # Mismatched length
            ),
            # Non-boolean Series
            (
                pd.DataFrame({"a": [1, 2, 3]}, index=["x", "y", "z"]),
                pd.Series([1, 0, 1], index=["x", "y", "z"]),  # Non-boolean values
            ),
            # Non-Series boolean index
            (
                pd.DataFrame({"a": [1, 2, 3]}, index=["x", "y", "z"]),
                [True, False, True],  # List instead of Series
            ),
        ]

    def test_boolean_indexing(self):
        """Test filtering DataFrame rows based on boolean Series."""
        for dataframe, boolean_series, expected_df in self.valid_test_cases:
            with self.subTest(dataframe=dataframe, boolean_series=boolean_series):
                retval = self.node.f(dataframe, boolean_series)[0]
                self.assertTrue(isinstance(retval, pd.DataFrame), "Expected DataFrame output.")
                pd.testing.assert_frame_equal(retval, expected_df)

    def test_invalid_inputs(self):
        """Test that invalid inputs raise errors."""
        for dataframe, boolean_series in self.invalid_test_cases:
            with self.subTest(dataframe=dataframe, boolean_series=boolean_series):
                with self.assertRaises(Exception):
                    self.node.f(dataframe, boolean_series)

if __name__ == "__main__":
    unittest.main()