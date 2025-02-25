import os
import sys
import unittest
import torch
import numpy as np

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_to_numpy import PtToNumpy

class TestPtToNumpy(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PtToNumpy()

        # Test cases covering rank 0 (scalar) to rank 5 tensors
        self.test_cases = [
            # Rank 0 (scalar) int32
            (torch.tensor(12345, dtype=torch.int32), np.array(12345, dtype=np.int32)),
            # Rank 0 (scalar) float32
            (torch.tensor(12345.6, dtype=torch.float32), np.array(12345.6, dtype=np.float32)),

            # Rank 1 (1D array) int32
            (torch.tensor([1, 2, 3], dtype=torch.int32), np.array([1, 2, 3], dtype=np.int32)),
            # Rank 1 (1D array) float32
            (torch.tensor([1.1, 2.2, 3.3], dtype=torch.float32), np.array([1.1, 2.2, 3.3], dtype=np.float32)),

            # Rank 2 (2D matrix) int32
            (torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int32), np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)),
            # Rank 2 (2D matrix) float32
            (torch.tensor([[1.1, 2.2], [3.3, 4.4]], dtype=torch.float32), np.array([[1.1, 2.2], [3.3, 4.4]], dtype=np.float32)),

            # Rank 3 (3D tensor) int32
            (torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=torch.int32),
             np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=np.int32)),
            # Rank 3 (3D tensor) float32
            (torch.tensor([[[1.1, 2.2], [3.3, 4.4]], [[5.5, 6.6], [7.7, 8.8]]], dtype=torch.float32),
             np.array([[[1.1, 2.2], [3.3, 4.4]], [[5.5, 6.6], [7.7, 8.8]]], dtype=np.float32)),
        ]

    def test_convert_tensor_to_numpy(self):
        """Test conversion of PyTorch tensor to NumPy ndarray."""
        for torch_tensor, expected_array in self.test_cases:
            with self.subTest(data=torch_tensor):
                retval = self.node.f(torch_tensor)[0]

                # Ensure the returned value is a NumPy array
                self.assertTrue(isinstance(retval, np.ndarray), f"Expected ndarray, got {type(retval)}")

                # Ensure the dtype matches
                self.assertEqual(retval.dtype, expected_array.dtype, f"Dtype mismatch for input: {torch_tensor}")

                # Ensure the shape matches
                self.assertEqual(retval.shape, expected_array.shape, 
                                 f"Shape mismatch for input: {torch_tensor} (Expected {expected_array.shape}, got {retval.shape})")

                # Ensure values match
                np.testing.assert_array_equal(retval, expected_array, 
                                              f"Value mismatch for input: {torch_tensor}")

if __name__ == "__main__":
    unittest.main()
