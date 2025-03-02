import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_rename_advanced import PandasRenameAdvanced

class TestPandasRenameAdvanced(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasRenameAdvanced()

        # Sample DataFrame
        self.df = pd.DataFrame(
            {
                "A": [1, 2, 3],
                "B": [4, 5, 6],
                100: [7, 8, 9],
            },
            index=["row1", "row2", 10]
        )

    def test_rename_columns_string(self):
        """Test renaming string column labels."""
        replacement_pairs = '{"A": "X", "B": "Y"}'
        expected_df = pd.DataFrame(
            {
                "X": [1, 2, 3],
                "Y": [4, 5, 6],
                100: [7, 8, 9],
            },
            index=["row1", "row2", 10]
        )
        result_df = self.node.f(self.df, "columns", replacement_pairs)[0]
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_rename_columns_integer(self):
        """Test renaming integer column labels."""
        replacement_pairs = '{100: 200}'
        expected_df = pd.DataFrame(
            {
                "A": [1, 2, 3],
                "B": [4, 5, 6],
                200: [7, 8, 9],
            },
            index=["row1", "row2", 10]
        )
        result_df = self.node.f(self.df, "columns", replacement_pairs)[0]
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_rename_index_string(self):
        """Test renaming string row labels."""
        replacement_pairs = '{"row1": "new_row1", "row2": "new_row2"}'
        expected_df = pd.DataFrame(
            {
                "A": [1, 2, 3],
                "B": [4, 5, 6],
                100: [7, 8, 9],
            },
            index=["new_row1", "new_row2", 10]
        )
        result_df = self.node.f(self.df, "index", replacement_pairs)[0]
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_rename_index_integer(self):
        """Test renaming integer row labels."""
        replacement_pairs = '{10: 20}'
        expected_df = pd.DataFrame(
            {
                "A": [1, 2, 3],
                "B": [4, 5, 6],
                100: [7, 8, 9],
            },
            index=["row1", "row2", 20]
        )
        result_df = self.node.f(self.df, "index", replacement_pairs)[0]
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_invalid_replacement_pairs_list(self):
        """Test invalid replacement_pairs format."""
        invalid_pairs = '{"A": ["X", "Y"]}'  # Not a valid mapping. List is not allowed.
        with self.assertRaises(ValueError):
            self.node.f(self.df, "columns", invalid_pairs)

    def test_invalid_replacement_pairs_dict(self):
        """Test invalid replacement_pairs format."""
        invalid_pairs = '{"A": {"X": "Y"}}'
        with self.assertRaises(ValueError):
            self.node.f(self.df, "columns", invalid_pairs)

    def test_invalid_replacement_pairs_tuple(self):
        """Test invalid replacement_pairs format."""
        invalid_pairs = '{"A": ()"X", "Y")}'
        with self.assertRaises(ValueError):
            self.node.f(self.df, "columns", invalid_pairs)

    def test_invalid_axis(self):
        """Test invalid axis value."""
        replacement_pairs = '{"A": "X"}'
        with self.assertRaises(ValueError):
            self.node.f(self.df, "invalid_axis", replacement_pairs)

if __name__ == "__main__":
    unittest.main()
