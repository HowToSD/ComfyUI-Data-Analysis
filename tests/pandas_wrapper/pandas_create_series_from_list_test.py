import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_create_series_from_list import PandasCreateSeriesFromList

class TestPandasCreateSeriesFromList(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasCreateSeriesFromList()
        self.valid_test_cases = [
            # Empty list
            ([], pd.Series([])),

            # List with single values
            ([12345], pd.Series([12345])),
            ([12345.6], pd.Series([12345.6])),
            (["apple"], pd.Series(["apple"])),
            ([True], pd.Series([True])),
            ([None], pd.Series([None])),
            
            # List with multiple values
            ([123, 456], pd.Series([123, 456])),
            ([1.5, 3.2, -7.8], pd.Series([1.5, 3.2, -7.8])),
            (["Alice", 30, "NYC"], pd.Series(["Alice", 30, "NYC"])),
            ([False, 99, 3.14159], pd.Series([False, 99, 3.14159]))
        ]

        self.invalid_test_cases = [
            # Non-list inputs
            None,
            {},
            (),
            "string",
            1234,
            56.78,
            {1, 2, 3},  # Set
            {"a": 1},  # Dict
        ]

    def test_create_series(self):
        """Test Series creation from lists."""
        for data, expected_series in self.valid_test_cases:
            with self.subTest(data=data):
                retval = self.node.f(data)[0]

                # Test if output is a Pandas Series
                self.assertTrue(isinstance(retval, pd.Series), f"Expected Series, got {type(retval)}")

                # Test if Series matches expected output
                pd.testing.assert_series_equal(retval, expected_series)

    def test_invalid_inputs(self):
        """Test that invalid inputs raise ValueError."""
        for data in self.invalid_test_cases:
            with self.subTest(data=data):
                with self.assertRaises(ValueError):
                    self.node.f(data)

if __name__ == "__main__":
    unittest.main()
