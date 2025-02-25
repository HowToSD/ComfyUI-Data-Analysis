import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pandas_wrapper.pandas_value_counts import PandasValueCounts

class TestPandasValueCounts(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.node = PandasValueCounts()

        self.df = pd.DataFrame({
            "Category": ["A", "B", "A", "C", "B", "A", "C"],
            "Numbers": [1, 2, 1, 3, 2, 1, 3],
            "Letter": ["X", "Y", "X", "Z", "Y", "X", "Z"],
            100: ["M", "N", "M", "O", "N", "M", "O"],  # Integer-labeled column
            200: [10, 20, 10, 30, 20, 10, 30]  # Another integer-labeled column
        })

    def test_single_string_column_label(self):
        """Test value_counts on a single string column label"""
        result = self.node.f(self.df, "Category")
        expected = self.df["Category"].value_counts().to_frame().rename(columns={"Category": "Count"}).reset_index().rename(columns={"index": "Category"})
        pd.testing.assert_frame_equal(result[0], expected)

    def test_single_integer_column_label(self):
        """Test value_counts on a single integer column label"""
        result = self.node.f(self.df, "100")
        expected = self.df[100].value_counts().to_frame().rename(columns={100: "Count"}).reset_index().rename(columns={"index": 100})
        pd.testing.assert_frame_equal(result[0], expected)

    def test_multiple_string_column_labels(self):
        """Test value_counts on multiple string column labels"""
        result = self.node.f(self.df, "Category,Letter")
        expected = self.df[["Category", "Letter"]].value_counts().to_frame().rename(columns={0:"Count"}).reset_index()
        pd.testing.assert_frame_equal(result[0], expected)

    def test_multiple_integer_column_labels(self):
        """Test value_counts on multiple integer column labels"""
        result = self.node.f(self.df, "100,200")
        expected = self.df[[100, 200]].value_counts().to_frame().rename(columns={0:"Count"}).reset_index()
        pd.testing.assert_frame_equal(result[0], expected)

    def test_mixed_string_integer_column_labels(self):
        """Test value_counts on a mix of string and integer column labels"""
        result = self.node.f(self.df, "Category,100")
        expected = self.df[["Category", 100]].value_counts().to_frame().rename(columns={0:"Count"}).reset_index()
        pd.testing.assert_frame_equal(result[0], expected)

if __name__ == "__main__":
    unittest.main()
