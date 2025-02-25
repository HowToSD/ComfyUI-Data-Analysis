import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_float_create import PtFloatCreate

class TestPtFloatCreate(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PtFloatCreate()

        # Test cases covering rank 0 (scalar) to rank 5 tensors
        self.test_cases = [
            # Rank 0 (scalar)
            ("12345", torch.tensor(12345, dtype=torch.float32)),
            ("12345.6", torch.tensor(12345.6, dtype=torch.float32)),

            # Rank 1 (1D array)
            ("[1, 2, 3]", torch.tensor([1, 2, 3], dtype=torch.float32)),
            ("[1.1, 2.2, 3.3]", torch.tensor([1.1, 2.2, 3.3], dtype=torch.float32)),

            # Rank 2 (2D matrix)
            ("[[1, 2, 3], [4, 5, 6]]", torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)),
            ("[[1.1, 2.2], [3.3, 4.4]]", torch.tensor([[1.1, 2.2], [3.3, 4.4]], dtype=torch.float32)),

            # Rank 3 (3D tensor)
            ("[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]", 
             torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=torch.float32)),
            
            # Rank 4 (4D tensor)
            ("[[[[1, 2], [3, 4]]], [[[5, 6], [7, 8]]]]", 
             torch.tensor([[[[1, 2], [3, 4]]], [[[5, 6], [7, 8]]]], dtype=torch.float32)),

            # Rank 5 (5D tensor)
            ("[[[[[1], [2]], [[3], [4]]]], [[[[5], [6]], [[7], [8]]]]]", 
             torch.tensor([[[[[1], [2]], [[3], [4]]]], [[[[5], [6]], [[7], [8]]]]], dtype=torch.float32)),
        ]

    def test_create_tensor(self):
        """Test PyTorch tensor creation from various structured inputs."""
        for data_str, expected_tensor in self.test_cases:
            with self.subTest(data=data_str):
                retval = self.node.f(data_str)[0]

                # Ensure the returned value is a PyTorch tensor
                self.assertTrue(isinstance(retval, torch.Tensor), f"Expected tensor, got {type(retval)}")

                # Ensure the dtype is float32
                self.assertEqual(retval.dtype, torch.float32, f"Dtype mismatch for input: {data_str}")

                # Ensure the shape matches
                self.assertEqual(retval.shape, expected_tensor.shape, 
                                 f"Shape mismatch for input: {data_str} (Expected {expected_tensor.shape}, got {retval.shape})")

                # Ensure values match
                torch.testing.assert_close(retval, expected_tensor, 
                                           msg=f"Value mismatch for input: {data_str}")

if __name__ == "__main__":
    unittest.main()
