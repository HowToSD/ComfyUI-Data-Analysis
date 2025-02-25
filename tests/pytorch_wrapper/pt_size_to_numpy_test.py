import os
import sys
import unittest
import torch
import numpy as np

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_size_to_numpy import PtSizeToNumpy

class TestPtSizeToNumpy(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PtSizeToNumpy()

        # Test cases with torch.Size objects
        self.test_cases = [
            # Empty size (zero-rank tensor shape)
            (torch.Size([]), np.array([], dtype=int)),
            # Rank 1 (single-dimension size)
            (torch.Size([3]), np.array([3], dtype=int)),
            # Rank 2 (matrix size)
            (torch.Size([3, 4]), np.array([3, 4], dtype=int)),
            # Rank 3 (3D tensor size)
            (torch.Size([2, 3, 4]), np.array([2, 3, 4], dtype=int)),
            # Rank 4 (higher-dimensional tensor size)
            (torch.Size([1, 2, 3, 4]), np.array([1, 2, 3, 4], dtype=int)),
            # Rank 5 (very high-dimensional tensor size)
            (torch.Size([5, 4, 3, 2, 1]), np.array([5, 4, 3, 2, 1], dtype=int)),
        ]

    def test_convert_size_to_numpy(self):
        """Test conversion of PyTorch Size to NumPy ndarray."""
        for torch_size, expected_array in self.test_cases:
            with self.subTest(data=torch_size):
                retval = self.node.f(torch_size)[0]

                # Ensure the returned value is a NumPy array
                self.assertTrue(isinstance(retval, np.ndarray), f"Expected ndarray, got {type(retval)}")

                # Ensure the dtype is integer
                self.assertEqual(retval.dtype, expected_array.dtype, f"Dtype mismatch for input: {torch_size}")

                # Ensure the shape matches
                self.assertEqual(retval.shape, expected_array.shape, 
                                 f"Shape mismatch for input: {torch_size} (Expected {expected_array.shape}, got {retval.shape})")

                # Ensure values match
                np.testing.assert_array_equal(retval, expected_array, 
                                              f"Value mismatch for input: {torch_size}")

if __name__ == "__main__":
    unittest.main()
