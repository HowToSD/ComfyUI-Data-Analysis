import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pandas_wrapper.pandas_crosstab import PandasCrosstab

class TestPandasCrosstab(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.node = PandasCrosstab()

        self.df = pd.DataFrame({
            "A": ["X", "X", "Y", "Y", "Z", "Z"],
            "B": ["M", "N", "M", "N", "M", "N"],
            "C": [1, 2, 3, 4, 5, 6],
            "D": [10, 20, 30, 40, 50, 60]
        })

    def test_crosstab_single_index_single_column(self):
        """Test crosstab with a single index and a single column"""
        result = self.node.f(self.df, index="A", column_names="B")[0]
        expected = pd.crosstab(index=self.df["A"], columns=self.df["B"])
        pd.testing.assert_frame_equal(result, expected)

    def test_crosstab_multi_index_single_column(self):
        """Test crosstab with multiple indices and a single column"""
        result = self.node.f(self.df, index="A,B", column_names="C")[0]
        expected = pd.crosstab(index=[self.df["A"], self.df["B"]], columns=self.df["C"])
        pd.testing.assert_frame_equal(result, expected)

    def test_crosstab_single_index_multi_column(self):
        """Test crosstab with a single index and multiple columns"""
        result = self.node.f(self.df, index="A", column_names="B,C")[0]
        expected = pd.crosstab(index=self.df["A"], columns=[self.df["B"], self.df["C"]])
        pd.testing.assert_frame_equal(result, expected)

    def test_crosstab_multi_index_multi_column(self):
        """Test crosstab with multiple indices and multiple columns"""
        result = self.node.f(self.df, index="A,B", column_names="C,D")[0]
        expected = pd.crosstab(index=[self.df["A"], self.df["B"]], columns=[self.df["C"], self.df["D"]])
        pd.testing.assert_frame_equal(result, expected)

    def test_crosstab_index_not_in_dataframe(self):
        """Test crosstab when the given index is not in the DataFrame"""
        with self.assertRaises(ValueError):
            self.node.f(self.df, index="Z", column_names="B")[0]

    def test_crosstab_columns_not_in_dataframe(self):
        """Test crosstab when the given column is not in the DataFrame"""
        with self.assertRaises(ValueError):
            self.node.f(self.df, index="A", column_names="Z")[0]

if __name__ == "__main__":
    unittest.main()
