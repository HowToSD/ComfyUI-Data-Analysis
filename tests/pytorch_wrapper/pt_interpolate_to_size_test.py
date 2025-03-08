import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_interpolate_to_size import PtInterpolateToSize


class TestPtInterpolateToSize(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtInterpolateToSize()

        # Test cases 3d: (Input tensor, Height, Width, Mode, Expected shape)
        self.test_cases_3d = [
            (torch.rand(3, 16, 16), 32, 32, "nearest", (3, 32, 32)),  # Upscale 3D tensor
            (torch.rand(3, 16, 16), 32, 32, "nearest-exact", (3, 32, 32)),  # Upscale 3D tensor
            (torch.rand(3, 16, 16), 8, 8, "bilinear", (3, 8, 8)),  # Downscale 3D tensor
            (torch.rand(3, 16, 16), 24, 24, "bicubic", (3, 24, 24)),  # Bicubic mode with 3D tensor
        ]

        # Test cases 4d: (Input tensor, Height, Width, Mode, Expected shape)
        self.test_cases_4d = [
            (torch.rand(1, 3, 16, 16), 32, 32, "nearest", (1, 3, 32, 32)),  # Upscale 4D tensor
            (torch.rand(1, 3, 16, 16), 32, 32, "nearest-exact", (1, 3, 32, 32)),  # Upscale 4D tensor
            (torch.rand(1, 3, 16, 16), 8, 8, "bilinear", (1, 3, 8, 8)),  # Downscale 4D tensor
            (torch.rand(1, 3, 16, 16), 24, 24, "bicubic", (1, 3, 24, 24)),  # Bicubic mode with 4D tensor
        ]

    def test_interpolation_3d(self):
        """Test tensor interpolation with different target sizes and modes."""
        for tens, height, width, mode, expected_shape in self.test_cases_3d:
            with self.subTest(height=height, width=width, mode=mode):
                result, = self.node.f(tens, height, width, mode)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result shape matches expected shape
                self.assertEqual(result.shape, expected_shape, f"Expected shape {expected_shape}, got {result.shape}")


    def test_interpolation_4d(self):
        """Test tensor interpolation with different target sizes and modes."""
        for tens, height, width, mode, expected_shape in self.test_cases_4d:
            with self.subTest(height=height, width=width, mode=mode):
                result, = self.node.f(tens, height, width, mode)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result shape matches expected shape
                self.assertEqual(result.shape, expected_shape, f"Expected shape {expected_shape}, got {result.shape}")


if __name__ == "__main__":
    unittest.main()
