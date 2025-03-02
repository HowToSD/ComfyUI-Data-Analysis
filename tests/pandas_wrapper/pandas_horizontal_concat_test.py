import os
import sys
import unittest
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pandas_wrapper.pandas_horizontal_concat import PandasHorizontalConcat


class TestPandasHorizontalConcat(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasHorizontalConcat()

        # Sample DataFrames
        self.df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        self.df2 = pd.DataFrame({"C": [5, 6], "D": [7, 8]})

    def test_concat_without_reset_labels(self):
        """Test horizontal concatenation without resetting column labels."""
        expected_df = pd.DataFrame({
            "A": [1, 2],
            "B": [3, 4],
            "C": [5, 6],
            "D": [7, 8]
        })

        retval = self.node.f(self.df1, self.df2, reset_labels=False)[0]
        pd.testing.assert_frame_equal(retval, expected_df)

    def test_concat_with_reset_labels(self):
        """Test horizontal concatenation with resetting column labels."""
        expected_df = pd.DataFrame({
            0: [1, 2],
            1: [3, 4],
            2: [5, 6],
            3: [7, 8]
        })

        retval = self.node.f(self.df1, self.df2, reset_labels=True)[0]
        pd.testing.assert_frame_equal(retval, expected_df)


if __name__ == "__main__":
    unittest.main()
