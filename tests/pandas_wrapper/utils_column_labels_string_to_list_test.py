import os
import sys
import unittest
import pandas as pd
from typing import List, Union

PROJECT_ROOT = os.path.realpath(os.path.join(__file__, "..", "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pandas_wrapper.utils import column_labels_string_to_list

class TestColumnLabelsStringToList(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.df = pd.DataFrame({
            "A": [1, 2, 3],
            "B": [4, 5, 6],
            "C": [7, 8, 9],
            10: [10, 11, 12],  # Integer column name
            20: [13, 14, 15]   # Another integer column name
        })

        self.no_check_labels = ["X", "Y"]

    def test_valid_column_strings(self):
        """Test valid column name conversion from string to list."""
        self.assertEqual(column_labels_string_to_list(self.df, "A,B"), ["A", "B"])
        self.assertEqual(column_labels_string_to_list(self.df, "C"), ["C"])

    def test_integer_column_labels(self):
        """Test conversion when integer column names are referenced as strings."""
        self.assertEqual(column_labels_string_to_list(self.df, "10"), [10])
        self.assertEqual(column_labels_string_to_list(self.df, "20"), [20])
        self.assertEqual(column_labels_string_to_list(self.df, "10,20"), [10, 20])

    def test_mixed_string_and_integer_columns(self):
        """Test function with mixed string and integer column labels."""
        self.assertEqual(column_labels_string_to_list(self.df, "A,10"), ["A", 10])
        self.assertEqual(column_labels_string_to_list(self.df, "B,20"), ["B", 20])

    def test_whitespace_handling(self):
        """Test that spaces around column names are stripped."""
        self.assertEqual(column_labels_string_to_list(self.df, " A , B "), ["A", "B"])
        self.assertEqual(column_labels_string_to_list(self.df, " 10 , 20 "), [10, 20])

    def test_non_existent_column(self):
        """Test behavior when a non-existent column is provided."""
        with self.assertRaises(ValueError) as context:
            column_labels_string_to_list(self.df, "D")
        self.assertIn("Column 'D' not found in the DataFrame.", str(context.exception))

    def test_mixed_valid_and_invalid_columns(self):
        """Test that function raises ValueError when a mix of valid and invalid columns is provided."""
        with self.assertRaises(ValueError) as context:
            column_labels_string_to_list(self.df, "A,D")
        self.assertIn("Column 'D' not found in the DataFrame.", str(context.exception))

    def test_invalid_integer_conversion(self):
        """Test that a string that can't be converted to an integer raises ValueError."""
        with self.assertRaises(ValueError) as context:
            column_labels_string_to_list(self.df, "A,xyz")
        self.assertIn("Column 'xyz' not found in the DataFrame.", str(context.exception))

    def test_no_check_labels(self):
        """Test no check labels"""
        self.assertEquals(
            column_labels_string_to_list(self.df, "X,Y", no_check=True),
            self.no_check_labels)


if __name__ == "__main__":
    unittest.main()

