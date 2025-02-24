import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pandas_wrapper.pandas_create_from_multiple_dict import PandasCreateFromMultipleDict

class TestPandasCreateFromMultipleDict(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasCreateFromMultipleDict()
        
        # Valid test cases with at least two dictionaries
        self.test_cases = [
            ({"a": [12345]}, {"b": [67890]}, pd.DataFrame({"a": [12345], "b": [67890]}, index=[0])),
            ({"a": [12345.6]}, {"b": [7890.1]}, pd.DataFrame({"a": [12345.6], "b": [7890.1]}, index=[0])),
            ({"a": ["apple"]}, {"b": ["banana"]}, pd.DataFrame({"a": ["apple"], "b": ["banana"]}, index=[0])),
            ({"a": [12345, 6789]}, {"b": [1111, 2222]}, pd.DataFrame({"a": [12345, 6789], "b": [1111, 2222]}, index=[0, 1])),
            ({"a": [123, 456]}, {"b": [789, 101]}, pd.DataFrame({"a": [123, 456], "b": [789, 101]}, index=[0, 1])),
        ]

        # Case where all 10 dictionaries are passed
        self.all_dicts_case = (
            {"a": [1, 2]}, {"b": [3, 4]}, {"c": [5, 6]}, {"d": [7, 8]}, {"e": [9, 10]},
            {"f": [11, 12]}, {"g": [13, 14]}, {"h": [15, 16]}, {"i": [17, 18]}, {"j": [19, 20]},
            pd.DataFrame({
                "a": [1, 2], "b": [3, 4], "c": [5, 6], "d": [7, 8], "e": [9, 10], 
                "f": [11, 12], "g": [13, 14], "h": [15, 16], "i": [17, 18], "j": [19, 20]
            }, index=[0, 1])
        )

        # Failure cases where first dictionary's value length differs from second's
        self.length_mismatch_cases = [
            ({"a": [1, 2]}, {"b": [3]}, "Length of the value elements are not the same."),
            ({"x": [10]}, {"y": [20, 30]}, "Length of the value elements are not the same."),
        ]

    def test_create_dataframe(self):
        """Test DataFrame creation from valid dictionary inputs."""
        for data1, data2, expected_df in self.test_cases:
            with self.subTest(data1=data1, data2=data2):
                retval = self.node.f(data1, data2)[0]  # Pass at least two dictionaries
                
                # Test if DataFrame structure matches
                self.assertTrue(isinstance(retval, pd.DataFrame))
                
                # Test if index matches
                self.assertTrue(retval.index.equals(expected_df.index), f"Index mismatch for input: {data1}, {data2}")

                # Test if data matches
                pd.testing.assert_frame_equal(retval, expected_df)

    def test_all_dicts(self):
        """Test case where all 10 dictionaries are provided."""
        data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, expected_df = self.all_dicts_case
        retval = self.node.f(data1, data2, data3, data4, data5, data6, data7, data8, data9, data10)[0]
        pd.testing.assert_frame_equal(retval, expected_df)

    def test_no_dict_failure(self):
        """Test failure when no dictionaries are passed."""
        with self.assertRaises(TypeError):
            self.node.f()  # No arguments should raise TypeError

    def test_length_mismatch_failure(self):
        """Test failure when first dictionary's value length differs from second's."""
        for data1, data2, error_message in self.length_mismatch_cases:
            with self.subTest(data1=data1, data2=data2):
                with self.assertRaises(ValueError) as context:
                    self.node.f(data1, data2)
                self.assertEqual(str(context.exception), error_message)


if __name__ == "__main__":
    unittest.main()
