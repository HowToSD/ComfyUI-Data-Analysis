import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pandas_wrapper.pandas_pivot import PandasPivot

class TestPandasPivot(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.node = PandasPivot()

        self.df = pd.DataFrame({
            "A": ["X", "X", "Y", "Y", "Z", "Z"],
            "B": ["M", "N", "M", "N", "M", "N"],
            "C": [1, 2, 3, 4, 5, 6],
            "D": [10, 20, 30, 40, 50, 60],
            "E": [100, 200, 300, 400, 500, 600]
        })

    def test_pivot_single_index_single_column(self):
        """Test pivot with a single index and a single column"""
        result = self.node.f(self.df, index="A", columns="B", values="C")[0]
        expected = self.df.pivot(index="A", columns="B", values="C")
        pd.testing.assert_frame_equal(result, expected)

    def test_pivot_multi_index_single_column(self):
        """Test pivot with multiple indices and a single column"""
        result = self.node.f(self.df, index="A,B", columns="C", values="D")[0]
        expected = self.df.pivot(index=["A", "B"], columns="C", values="D")
        pd.testing.assert_frame_equal(result, expected)

    def test_pivot_single_index_multi_column(self):
        """Test pivot with a single index and multiple columns"""
        result = self.node.f(self.df, index="A", columns="B,C", values="D")[0]
        expected = self.df.pivot(index="A", columns=["B", "C"], values="D")
        pd.testing.assert_frame_equal(result, expected)

    def test_pivot_multi_index_multi_column(self):
        """Test pivot with multiple indices and multiple columns"""
        result = self.node.f(self.df, index="A,B", columns="C,E", values="D")[0]
        expected = self.df.pivot(index=["A", "B"], columns=["C", "E"], values="D")
        pd.testing.assert_frame_equal(result, expected)

    def test_pivot_single_index_multi_values(self):
        """Test pivot with a single index and multiple value columns"""
        result = self.node.f(self.df, index="A", columns="B", values="C,D")[0]
        expected = self.df.pivot(index="A", columns="B", values=["C", "D"])
        pd.testing.assert_frame_equal(result, expected)

    def test_pivot_multi_index_multi_values(self):
        """Test pivot with multiple indices and multiple value columns"""
        result = self.node.f(self.df, index="A,B", columns="C", values="D,E")[0]
        expected = self.df.pivot(index=["A", "B"], columns="C", values=["D", "E"])
        pd.testing.assert_frame_equal(result, expected)

    def test_pivot_index_not_in_dataframe(self):
        """Test pivot when the given index is not in the DataFrame"""
        with self.assertRaises(ValueError):
            self.node.f(self.df, index="Z", columns="B", values="C")[0]

    def test_pivot_columns_not_in_dataframe(self):
        """Test pivot when the given column is not in the DataFrame"""
        with self.assertRaises(ValueError):
            self.node.f(self.df, index="A", columns="Z", values="C")[0]

    def test_pivot_values_not_in_dataframe(self):
        """Test pivot when the given value column is not in the DataFrame"""
        with self.assertRaises(ValueError):
            self.node.f(self.df, index="A", columns="B", values="Z")[0]

    def test_pivot_duplicate_index_column_pairs(self):
        """Test pivot when index-column pairs are not unique (should raise an error)"""
        df_dup = self.df.copy()
        df_dup.loc[1, "B"] = "M"  # Introduce a duplicate index-column pair
        with self.assertRaises(ValueError):
            self.node.f(df_dup, index="A", columns="B", values="C")[0]

    def test_pivot_from_long_to_wide(self):
        """Test pivot where column labels become row values before pivoting.
        This is the test case referenced in the docstring."""
        df_long = pd.DataFrame({
            "R": ["A", "A", "A", "B", "B", "B", "C", "C", "C"],
            "C": ["X", "Y", "Z", "X", "Y", "Z", "X", "Y", "Z"],
            "V": [1, 2, 3, 4, 5, 6, 7, 8, 9]
        })

        result = self.node.f(df_long, index="R", columns="C", values="V")[0]
        expected = pd.DataFrame({
            "X": [1, 4, 7],
            "Y": [2, 5, 8],
            "Z": [3, 6, 9]
        }, index=["A", "B", "C"])

        # Explicitly set index and column names to match pivot output
        expected.index.name = "R"
        expected.columns.name = "C"

        pd.testing.assert_frame_equal(result, expected)


if __name__ == "__main__":
    unittest.main()
