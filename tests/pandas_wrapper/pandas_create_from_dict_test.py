import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_create_from_dict import PandasCreateFromDict

class TestPandasCreateFromDict(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasCreateFromDict()
        self.test_cases = [
            ({"a": 12345}, pd.DataFrame({"a": [12345]}, index=[0])),
            ({"a": 12345.6}, pd.DataFrame({"a": [12345.6]}, index=[0])),
            ({"a": "apple"}, pd.DataFrame({"a": ["apple"]}, index=[0])),
            ({"a": [12345, 6789]}, pd.DataFrame({"a": [12345, 6789]}, index=[0, 1])),
            ({"a": [12345.6, 7890.1]}, pd.DataFrame({"a": [12345.6, 7890.1]}, index=[0, 1])),
            ({"a": ["apple", "banana"]}, pd.DataFrame({"a": ["apple", "banana"]}, index=[0, 1])),
            ({"a": 123, "b": 456}, pd.DataFrame({"a": [123], "b": [456]}, index=[0])),
            ({"a": 12.3, "b": 45.6}, pd.DataFrame({"a": [12.3], "b": [45.6]}, index=[0])),
            ({"a": "foo", "b": "bar"}, pd.DataFrame({"a": ["foo"], "b": ["bar"]}, index=[0])),
            ({"a": [1, 2], "b": [3, 4]}, pd.DataFrame({"a": [1, 2], "b": [3, 4]}, index=[0, 1])),
            ({"a": [1.1, 2.2], "b": [3.3, 4.4]}, pd.DataFrame({"a": [1.1, 2.2], "b": [3.3, 4.4]}, index=[0, 1])),
            ({"a": ["x", "y"], "b": ["z", "w"]}, pd.DataFrame({"a": ["x", "y"], "b": ["z", "w"]}, index=[0, 1]))
        ]

    def test_create_dataframe(self):
        """Test DataFrame creation from various dictionary inputs."""
        for data, expected_df in self.test_cases:
            with self.subTest(data=data):
                retval = self.node.f(data)[0]
                
                # Test if DataFrame structure matches
                self.assertTrue(isinstance(retval, pd.DataFrame))
                
                # Test if index matches
                self.assertTrue(retval.index.equals(expected_df.index), f"Index mismatch for input: {data}")

                # Test if data matches
                pd.testing.assert_frame_equal(retval, expected_df)

if __name__ == "__main__":
    unittest.main()
