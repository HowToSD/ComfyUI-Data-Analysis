import os
import sys
import unittest
import numpy as np
import pandas as pd
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pandas_wrapper.pandas_feature_split_to_pt import PandasFeatureSplitToPt

class TestPandasFeatureSplitToPt(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasFeatureSplitToPt()

        # Sample DataFrame
        self.df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        })

    def test_feature_split(self):
        """Test splitting with different label positions."""
        test_cases = [
            (0, True, [[4, 7], [5, 8], [6, 9]], [1, 2, 3]),
            (1, True, [[1, 7], [2, 8], [3, 9]], [4, 5, 6]),
            (2, True, [[1, 4], [2, 5], [3, 6]], [7, 8, 9]),
            (-1, True, [[1, 4], [2, 5], [3, 6]], [7, 8, 9]),
        ]
        
        data_types = ["float32", "float16", "bfloat16", "float64", "int8", "uint8", "int16", "int32", "int64"]
        for feature_dtype in data_types:
            for label_dtype in data_types:
                for label_pos, output_1d, expected_features, expected_labels in test_cases:
                    with self.subTest(label_pos=label_pos, output_1d=output_1d, feature_dtype=feature_dtype, label_dtype=label_dtype):
                        features, labels = self.node.f(self.df, label_pos, output_1d, feature_dtype, label_dtype)
                        torch.testing.assert_close(features, torch.tensor(expected_features, dtype=getattr(torch, feature_dtype)))
                        torch.testing.assert_close(labels, torch.tensor(expected_labels, dtype=getattr(torch, label_dtype)))

    def test_invalid_label_position(self):
        """Test invalid label positions."""
        with self.assertRaises(ValueError):
            self.node.f(self.df, 3, True, "float32", "int64")

if __name__ == "__main__":
    unittest.main()
