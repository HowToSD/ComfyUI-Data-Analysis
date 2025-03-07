import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_create_series_from_list_index_list import PandasCreateSeriesFromListIndexList

class TestPandasCreateSeriesFromListIndexList(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasCreateSeriesFromListIndexList()
        self.valid_test_cases = [
            # Empty list
            ([], [], pd.Series([])),

            # List with single values
            ([12345], ["a"], pd.Series([12345], index=["a"])),
            ([12345.6], [1], pd.Series([12345.6], index=[1])),
            (["apple"], ["fruit"], pd.Series(["apple"], index=["fruit"])),
            ([True], ["flag"], pd.Series([True], index=["flag"])),
            ([None], ["null"], pd.Series([None], index=["null"])),
            
            # List with multiple values
            ([123, 456], ["a", "b"], pd.Series([123, 456], index=["a", "b"])),
            ([1.5, 3.2, -7.8], ["x", "y", "z"], pd.Series([1.5, 3.2, -7.8], index=["x", "y", "z"])),
            (["Alice", 30, "NYC"], ["name", "age", "city"], pd.Series(["Alice", 30, "NYC"], index=["name", "age", "city"])),
            ([False, 99, 3.14159], ["flag", "score", "pi"], pd.Series([False, 99, 3.14159], index=["flag", "score", "pi"]))
        ]

        self.invalid_test_cases_value_error = [
            # Non-list inputs
            (None, []),
            ({}, []),
            ((), []),
            ("string", []),
            (1234, []),
            (56.78, []),
            ({1, 2, 3}, []),  # Set
            ({"a": 1}, []),  # Dict
            ([1, 2], ["a"])  # Mismatched data and index length
        ]

        self.invalid_test_cases_type_error = [
            ([1, 2, 3], "invalid"),  # Invalid index type
        ]

    def test_create_series(self):
        """Test Series creation from lists with index."""
        for data, index, expected_series in self.valid_test_cases:
            with self.subTest(data=data, index=index):
                retval = self.node.f(data, index)[0]

                # Test if output is a Pandas Series
                self.assertTrue(isinstance(retval, pd.Series), f"Expected Series, got {type(retval)}")

                # Test if Series matches expected output
                pd.testing.assert_series_equal(retval, expected_series)

    def test_invalid_inputs_type_error(self):
        """Test that invalid inputs raise TypeError."""
        for data, index in self.invalid_test_cases_type_error:
            with self.subTest(data=data, index=index):
                with self.assertRaises(TypeError):
                    self.node.f(data, index)

    def test_invalid_inputs_value_error(self):
        """Test that invalid inputs raise ValueError."""
        for data, index in self.invalid_test_cases_value_error:
            with self.subTest(data=data, index=index):
                with self.assertRaises(ValueError):
                    self.node.f(data, index)


if __name__ == "__main__":
    unittest.main()