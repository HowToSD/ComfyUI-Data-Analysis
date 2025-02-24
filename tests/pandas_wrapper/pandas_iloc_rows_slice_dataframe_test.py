import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pandas_wrapper.pandas_iloc_rows_slice_dataframe import PandasIlocRowsSliceDataFrame

class Test(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.node = PandasIlocRowsSliceDataFrame()

        self.df = pd.DataFrame({
            "purchase_price": [2, 3, 4, 6, 8, 5, 6],
            "sales_price": [3, 6, 5, 7, 10, 4, 3],
            "in_stock": ["Yes", "No", "Yes", "No", "Yes", "Yes", "Yes"]
        }, index=["apple", "banana", "coconut", "donut", "egg", "fig", "guava"])
    
    def test_iloc_rows_slice(self):
        """Test row slicing functionality"""
        result_df, = self.node.f(self.df, 1, 4)
        expected_df = self.df.iloc[1:4]
        pd.testing.assert_frame_equal(result_df, expected_df)

if __name__ == "__main__":
    unittest.main()