import os
import sys
import unittest
import torch


PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_from_image_transpose import PtFromImageTranspose


class TestPtFromImageTranspose(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtFromImageTranspose()

        # Define test cases: (input_tensor, expected_shape)
        self.test_cases = [
            # Case 1: 3D tensor (H, W, C) -> (C, H, W)
            (torch.ones(64, 128, 3), (3, 64, 128)),  # (64,128,3) -> (3,64,128)

            # Case 2: 4D tensor (N, H, W, C) -> (N, C, H, W)
            (torch.ones(10, 64, 128, 3), (10, 3, 64, 128)),  # (10,64,128,3) -> (10,3,64,128)

            # Case 3: Invalid input (2D tensor)
            (torch.ones(64, 128), ValueError),  # 2D tensors should raise an error

            # Case 4: Invalid input (5D tensor)
            (torch.ones(10, 64, 128, 3, 2), ValueError),  # 5D tensors should raise an error
        ]

    def test_transpose(self):
        """Test image transposition operation with valid and invalid cases."""
        for input_tensor, expected in self.test_cases:
            with self.subTest(input_shape=input_tensor.shape):
                if isinstance(expected, tuple):
                    # Valid cases
                    result, = self.node.f(input_tensor)

                    # Ensure return value is a tensor
                    self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                    # Ensure result has correct shape
                    self.assertEqual(result.shape, torch.Size(expected), f"Expected shape {expected}, got {result.shape}")

                    # Ensure result has the same dtype
                    self.assertEqual(result.dtype, input_tensor.dtype, "Dtype mismatch after transpose operation")
                else:
                    # Invalid cases should raise an error
                    with self.assertRaises(expected):
                        self.node.f(input_tensor)


if __name__ == "__main__":
    unittest.main()
