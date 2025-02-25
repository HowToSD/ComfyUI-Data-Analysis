import os
import sys
import unittest
import torch
import numpy as np

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_from_numpy import PtFromNumpy


class TestPtFromNumpy(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PtFromNumpy()

        # Test cases covering rank 0 (scalar) to rank 3 tensors
        self.test_cases = [
            # Rank 0 (scalar) int32
            (np.array(12345, dtype=np.int32), torch.tensor(12345, dtype=torch.int32)),
            # Rank 0 (scalar) float32
            (np.array(12345.6, dtype=np.float32), torch.tensor(12345.6, dtype=torch.float32)),

            # Rank 1 (1D array) int32
            (np.array([1, 2, 3], dtype=np.int32), torch.tensor([1, 2, 3], dtype=torch.int32)),
            # Rank 1 (1D array) float32
            (np.array([1.1, 2.2, 3.3], dtype=np.float32), torch.tensor([1.1, 2.2, 3.3], dtype=torch.float32)),

            # Rank 2 (2D matrix) int32
            (np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32), torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.int32)),
            # Rank 2 (2D matrix) float32
            (np.array([[1.1, 2.2], [3.3, 4.4]], dtype=np.float32), torch.tensor([[1.1, 2.2], [3.3, 4.4]], dtype=torch.float32)),

            # Rank 3 (3D tensor) int32
            (np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=np.int32),
             torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=torch.int32)),
            # Rank 3 (3D tensor) float32
            (np.array([[[1.1, 2.2], [3.3, 4.4]], [[5.5, 6.6], [7.7, 8.8]]], dtype=np.float32),
             torch.tensor([[[1.1, 2.2], [3.3, 4.4]], [[5.5, 6.6], [7.7, 8.8]]], dtype=torch.float32)),
        ]

    def test_convert_numpy_to_tensor(self):
        """Test conversion of NumPy ndarray to PyTorch tensor."""
        for np_array, expected_tensor in self.test_cases:
            with self.subTest(data=np_array):
                retval = self.node.f(np_array)[0]

                # Ensure the returned value is a PyTorch tensor
                self.assertTrue(isinstance(retval, torch.Tensor), f"Expected tensor, got {type(retval)}")

                # Ensure the dtype matches
                self.assertEqual(retval.dtype, expected_tensor.dtype, f"Dtype mismatch for input: {np_array}")

                # Ensure the shape matches
                self.assertEqual(retval.shape, expected_tensor.shape, 
                                 f"Shape mismatch for input: {np_array} (Expected {expected_tensor.shape}, got {retval.shape})")

                # Ensure values match
                torch.testing.assert_close(retval, expected_tensor, 
                                           msg=f"Value mismatch for input: {np_array}")

if __name__ == "__main__":
    unittest.main()
