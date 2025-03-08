import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_pad import PtPad


class TestPtPad(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtPad()

        # Test cases: (Input tensor, Height, Width, Expected shape)
        self.test_cases = [
            (torch.rand(1, 3, 16, 16), 32, 32, (1, 3, 32, 32)),  # Pad 4D tensor
            (torch.rand(3, 16, 16), 32, 32, (3, 32, 32)),  # Pad 3D tensor
            (torch.rand(1, 3, 16, 16), 16, 16, (1, 3, 16, 16)),  # No padding, same size
        ]

    def test_padding(self):
        """Test tensor padding to specific sizes."""
        for tens, height, width, expected_shape in self.test_cases:
            with self.subTest(height=height, width=width):
                result, = self.node.f(tens, height, width)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result shape matches expected shape
                self.assertEqual(result.shape, expected_shape, f"Expected shape {expected_shape}, got {result.shape}")

    def test_invalid_tensor_rank(self):
        """Test that an invalid tensor rank raises an error."""
        tens = torch.rand(16, 16)  # 2D tensor (invalid)
        with self.assertRaises(ValueError, msg="Only rank 3 or 4 tensors are supported for padding."):
            self.node.f(tens, 32, 32)

    def test_padding_smaller_than_tensor(self):
        """Test that padding to a smaller size raises an error."""
        tens = torch.rand(1, 3, 16, 16)
        with self.assertRaises(ValueError, msg="Specified dimensions must be greater than or equal to tensor dimensions."):
            self.node.f(tens, 8, 8)

if __name__ == "__main__":
    unittest.main()
