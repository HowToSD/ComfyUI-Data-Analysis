import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.utils import column_label_string_to_target_type

class TestColumnLabelStringToTargetType(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.df = pd.DataFrame({
            "A": [1, 2, 3],
            "B": [4, 5, 6],
            "C": [7, 8, 9],
            10: [10, 11, 12],  # Integer column name
            20: [13, 14, 15],  # Another integer column name
            3.5: [16, 17, 18]  # Float column name
        })

    def test_valid_string_column(self):
        """Test valid string column names remain unchanged."""
        self.assertEqual(column_label_string_to_target_type(self.df, "A"), "A")
        self.assertEqual(column_label_string_to_target_type(self.df, "B"), "B")

    def test_integer_column_labels(self):
        """Test conversion when integer column names are referenced as strings."""
        self.assertEqual(column_label_string_to_target_type(self.df, "10"), 10)
        self.assertEqual(column_label_string_to_target_type(self.df, "20"), 20)

    def test_float_column_label(self):
        """Test conversion when float column names are referenced as strings."""
        self.assertEqual(column_label_string_to_target_type(self.df, "3.5"), 3.5)

    def test_whitespace_handling(self):
        """Test that spaces around column names are stripped before conversion."""
        self.assertEqual(column_label_string_to_target_type(self.df, " A "), "A")
        self.assertEqual(column_label_string_to_target_type(self.df, " 10 "), 10)
        self.assertEqual(column_label_string_to_target_type(self.df, " 3.5 "), 3.5)

    def test_non_existent_column(self):
        """Test behavior when a non-existent column is provided."""
        with self.assertRaises(ValueError) as context:
            column_label_string_to_target_type(self.df, "D")
        self.assertIn("Column 'D' not found in the DataFrame.", str(context.exception))

    def test_non_existent_column_with_return_none(self):
        """Test behavior when a non-existent column is provided."""
        retval = column_label_string_to_target_type(self.df, "D", return_none=True)
        self.assertTrue(retval is None)

    def test_invalid_integer_conversion(self):
        """Test that a string that can't be converted to an integer or float raises ValueError."""
        with self.assertRaises(ValueError) as context:
            column_label_string_to_target_type(self.df, "xyz")
        self.assertIn("Column 'xyz' not found in the DataFrame.", str(context.exception))

if __name__ == "__main__":
    unittest.main()
