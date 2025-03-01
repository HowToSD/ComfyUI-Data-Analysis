import os
import sys
import unittest
import numpy as np
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pandas_wrapper.pandas_feature_split_to_numpy import PandasFeatureSplitToNumpy

class TestPandasFeatureSplitToNumpy(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasFeatureSplitToNumpy()

        # Sample DataFrame
        self.df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        })

    def test_feature_split_last_column_label_0(self):
        """Test splitting with the last column as the label."""
        features, labels = self.node.f(self.df, label_integer_position=0, output_1d_label=True)

        np.testing.assert_array_equal(features, np.array([[4, 7], [5, 8], [6, 9]]))
        np.testing.assert_array_equal(labels, np.array([1, 2, 3]))

    def test_feature_split_last_column_label_1(self):
        """Test splitting with the last column as the label."""
        features, labels = self.node.f(self.df, label_integer_position=1, output_1d_label=True)

        np.testing.assert_array_equal(features, np.array([[1, 7], [2, 8], [3, 9]]))
        np.testing.assert_array_equal(labels, np.array([4, 5, 6]))

    def test_feature_split_last_column_label_2(self):
        """Test splitting with the last column as the label."""
        features, labels = self.node.f(self.df, label_integer_position=2, output_1d_label=True)

        np.testing.assert_array_equal(features, np.array([[1, 4], [2, 5], [3, 6]]))
        np.testing.assert_array_equal(labels, np.array([7, 8, 9]))

    def test_feature_split_last_column_label_negative_1(self):
        """Test splitting with the last column as the label."""
        features, labels = self.node.f(self.df, label_integer_position=-1, output_1d_label=True)

        np.testing.assert_array_equal(features, np.array([[1, 4], [2, 5], [3, 6]]))
        np.testing.assert_array_equal(labels, np.array([7, 8, 9]))


if __name__ == "__main__":
    unittest.main()
