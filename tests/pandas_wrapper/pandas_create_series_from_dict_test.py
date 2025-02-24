import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_create_series_from_dict import PandasCreateSeriesFromDict

class TestPandasCreateSeriesFromDict(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasCreateSeriesFromDict()
        self.valid_test_cases = [
            # Empty dict
            ({}, pd.Series({})),

            # Single key-value pairs
            ({"a": 12345}, pd.Series({"a": 12345})),
            ({"a": 12345.6}, pd.Series({"a": 12345.6})),
            ({"a": "apple"}, pd.Series({"a": "apple"})),
            ({"a": True}, pd.Series({"a": True})),
            ({"a": None}, pd.Series({"a": None})),  # None should be treated as a valid value
            
            # Multiple key-value pairs
            ({"a": 123, "b": 456}, pd.Series({"a": 123, "b": 456})),
            ({"x": 1.5, "y": 3.2, "z": -7.8}, pd.Series({"x": 1.5, "y": 3.2, "z": -7.8})),
            ({"name": "Alice", "age": 30, "city": "NYC"}, pd.Series({"name": "Alice", "age": 30, "city": "NYC"})),
            ({"flag": False, "score": 99, "pi": 3.14159}, pd.Series({"flag": False, "score": 99, "pi": 3.14159})),
        ]

        self.invalid_test_cases = [
            # Non-dictionary inputs
            None,
            [],
            (),
            "string",
            1234,
            56.78,
            {1, 2, 3},  # Set
            [{"a": 1}],  # List containing a dict
            
            # Dictionaries with non-scalar values
            {"a": [12345, 6789]},  # List value
            {"a": {"key": "value"}},  # Dict value
            {"a": (1, 2)},  # Tuple value
            {"a": {1, 2}},  # Set value
            
            # Mixed valid and invalid values
            {"a": 123, "b": [456, 789]},  # One scalar, one list
            {"x": 1.5, "y": {"nested": "dict"}},  # One scalar, one dict
            {"flag": False, "data": (3, 4)},  # One scalar, one tuple
        ]

    def test_create_series(self):
        """Test Series creation from dictionaries with multiple key-value pairs."""
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
