import os
import sys
import unittest
import torch
import pandas as pd

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)
from pandas_wrapper.pandas_create_from_tensor import PandasCreateFromTensor

class TestPandasCreateFromTensor(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PandasCreateFromTensor()
        
        self.test_cases = [
            # Rank 0 (Invalid)
            (torch.tensor(42), ValueError),
            (torch.tensor(3.14), ValueError),
            (torch.tensor(True), ValueError),
            
            # Rank 1 (Valid)
            (torch.tensor([1, 2, 3], dtype=torch.float32), pd.DataFrame([1, 2, 3], dtype="float32")),
            (torch.tensor([1.1, 2.2, 3.3], dtype=torch.float32), pd.DataFrame([1.1, 2.2, 3.3], dtype="float32")),
            (torch.tensor([True, False, True], dtype=torch.float32), pd.DataFrame([1.0, 0.0, 1.0], dtype="float32")),
            
            # Rank 2 (Valid)
            (torch.tensor([[1, 2], [3, 4]], dtype=torch.float32), pd.DataFrame([[1, 2], [3, 4]], dtype="float32")),
            (torch.tensor([[1.1, 2.2], [3.3, 4.4]], dtype=torch.float32), pd.DataFrame([[1.1, 2.2], [3.3, 4.4]], dtype="float32")),
            
            # Rank 3+ (Invalid)
            (torch.rand(2, 2, 2), ValueError),
            (torch.rand(2, 2, 2, 2), ValueError),
        ]
    
    def test_create_dataframe(self):
        """Test DataFrame creation from various PyTorch tensors."""
        for data, expected in self.test_cases:
            with self.subTest(data=data):
                if isinstance(expected, type) and issubclass(expected, Exception):
                    with self.assertRaises(expected):
                        self.node.f(data)
                else:
                    retval = self.node.f(data)[0]
                    
                    # Test if DataFrame structure matches
                    self.assertTrue(isinstance(retval, pd.DataFrame))
                    
                    # Test if data matches
                    pd.testing.assert_frame_equal(retval, expected)

if __name__ == "__main__":
    unittest.main()
