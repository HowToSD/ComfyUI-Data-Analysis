import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_create_from_dict_index_list import PandasCreateFromDictIndexList

class TestPandasCreateFromDictIndexList(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasCreateFromDictIndexList()
        self.test_cases = [
            # Test with a standard dictionary and provided index
            (
                {"a": [1, 2, 3], "b": [4, 5, 6]},
                ["row1", "row2", "row3"],
                pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, index=["row1", "row2", "row3"])
            ),
            # Test with an empty dictionary (should return an empty DataFrame)
            (
                {},
                ["row1", "row2"],
                pd.DataFrame()
            ),
            # Test with missing index (should use default range index)
            (
                {"a": [7, 8, 9]},
                None,
                pd.DataFrame({"a": [7, 8, 9]}, index=[0, 1, 2])
            ),
            # Test with integer index values
            (
                {"x": [10, 20], "y": [30, 40]},
                [100, 101],
                pd.DataFrame({"x": [10, 20], "y": [30, 40]}, index=[100, 101])
            ),
            # Test with a single column and mismatched index length (should raise an error)
            (
                {"c": [1, 2]},
                ["only_one_row"],
                ValueError  # Expecting an error because index length doesn't match data length
            ),
        ]

    def test_create_dataframe(self):
        """Test creating a pandas DataFrame from a dictionary with an index."""
        for data, index, expected in self.test_cases:
            with self.subTest(data=data, index=index):
                if expected is ValueError:
                    with self.assertRaises(ValueError):
                        self.node.f(data, index)
                else:
                    retval = self.node.f(data, index)
                    self.assertIsInstance(retval, tuple, "Return value should be a tuple.")
                    self.assertEqual(len(retval), 1, "Return tuple should have a single DataFrame.")
                    pd.testing.assert_frame_equal(retval[0], expected)

if __name__ == "__main__":
    unittest.main()
