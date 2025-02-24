import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pandas_wrapper.pandas_melt import PandasMelt

class TestPandasMelt(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.node = PandasMelt()

        self.df = pd.DataFrame({
            "Manufacturer": ["Aimee Italian Foods", "Olivia Cuisine", "Maddie Foods"],
            "Pizza": [10, 11, 12],
            "Burger": [12, 8, 7]
        })

    def test_pandas_melt_single_column(self):
        """Test melting a single column"""
        result_df = self.node.f(
            dataframe=self.df,
            id_vars="Manufacturer",
            value_vars="Pizza",
            var_name="Item",
            value_name="Price",
            ignore_index=True
        )[0]  # Extract DataFrame

        expected_df = pd.DataFrame({
            "Manufacturer": ["Aimee Italian Foods", "Olivia Cuisine", "Maddie Foods"],
            "Item": ["Pizza", "Pizza", "Pizza"],
            "Price": [10, 11, 12]
        })

        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_pandas_melt_multiple_columns(self):
        """Test melting multiple columns"""
        result_df = self.node.f(
            dataframe=self.df,
            id_vars="Manufacturer",
            value_vars="Pizza,Burger",
            var_name="Item",
            value_name="Price",
            ignore_index=True
        )[0]  # Extract DataFrame

        expected_df = pd.DataFrame({
            "Manufacturer": [
                "Aimee Italian Foods", "Olivia Cuisine", "Maddie Foods",
                "Aimee Italian Foods", "Olivia Cuisine", "Maddie Foods"
            ],
            "Item": ["Pizza", "Pizza", "Pizza", "Burger", "Burger", "Burger"],
            "Price": [10, 11, 12, 12, 8, 7]
        })

        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_pandas_melt_ignore_index_true(self):
        """Test melting with ignore_index=True"""
        # Modify the original DataFrame to have a custom index
        self.df.index = pd.Index([10, 20, 30])  # Explicitly set a non-default index

        result_df = self.node.f(
            dataframe=self.df,
            id_vars="Manufacturer",
            value_vars="Pizza,Burger",
            var_name="Item",
            value_name="Price",
            ignore_index=True
        )[0]  # Extract DataFrame

        expected_df = pd.DataFrame({
            "Manufacturer": [
                "Aimee Italian Foods", "Olivia Cuisine", "Maddie Foods",
                "Aimee Italian Foods", "Olivia Cuisine", "Maddie Foods"
            ],
            "Item": ["Pizza", "Pizza", "Pizza", "Burger", "Burger", "Burger"],
            "Price": [10, 11, 12, 12, 8, 7]
        })

        # Check the data itself
        pd.testing.assert_frame_equal(result_df, expected_df, check_index_type=False)

        # Explicitly verify that the index is reset to a sequential range
        expected_index = pd.RangeIndex(start=0, stop=len(expected_df), step=1)
        self.assertTrue(result_df.index.equals(expected_index), "Index is not fully reset.")

    def test_pandas_melt_ignore_index_false(self):
        """Test melting with ignore_index=False"""
        self.df.index = pd.Index([10, 20, 30])  # Explicitly set a non-default index

        result_df = self.node.f(
            dataframe=self.df,
            id_vars="Manufacturer",
            value_vars="Pizza,Burger",
            var_name="Item",
            value_name="Price",
            ignore_index=False
        )[0]  # Extract DataFrame

        expected_df = pd.DataFrame({
            "Manufacturer": [
                "Aimee Italian Foods", "Olivia Cuisine", "Maddie Foods",
                "Aimee Italian Foods", "Olivia Cuisine", "Maddie Foods"
            ],
            "Item": ["Pizza", "Pizza", "Pizza", "Burger", "Burger", "Burger"],
            "Price": [10, 11, 12, 12, 8, 7]
        }, index=[10, 20, 30, 10, 20, 30])  # Correctly retain and repeat original index

        # Compare both data and index
        pd.testing.assert_frame_equal(result_df, expected_df)

        # Explicitly verify that the index is correctly retained and repeated
        expected_index = pd.Index([10, 20, 30, 10, 20, 30])  
        self.assertTrue(result_df.index.equals(expected_index), "Index was not retained correctly.")


if __name__ == "__main__":
    unittest.main()
