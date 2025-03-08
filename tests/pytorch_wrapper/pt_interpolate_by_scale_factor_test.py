import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_interpolate_by_scale_factor import PtInterpolateByScaleFactor


class TestPtInterpolateByScaleFactor(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtInterpolateByScaleFactor()

        # Test cases 3d: (Input tensor, Scale factor, Mode, Expected shape)
        self.test_cases_3d = [
            (torch.rand(3, 16, 16), 2.0, "nearest", (3, 32, 32)),
            (torch.rand(3, 16, 16), 2.0, "nearest-exact", (3, 32, 32)),
            (torch.rand(3, 16, 16), 0.5, "bilinear", (3, 8, 8)),
            (torch.rand(3, 16, 16), 1.5, "bicubic", (3, 24, 24)),
        ]

        # Test cases: (Input tensor, Scale factor, Mode, Expected shape)
        self.test_cases_4d = [
            (torch.rand(1, 3, 16, 16), 2.0, "nearest", (1, 3, 32, 32)),  # Upscale 4D tensor
            (torch.rand(1, 3, 16, 16), 2.0, "nearest-exact", (1, 3, 32, 32)),  # Upscale 4D tensor
            (torch.rand(1, 3, 16, 16), 0.5, "bilinear", (1, 3, 8, 8)),  # Downscale 4D tensor
            (torch.rand(1, 3, 16, 16), 1.5, "bicubic", (1, 3, 24, 24)),  # Bicubic mode with 4D tensor
        ]

    def test_interpolation_3d(self):
        """Test tensor interpolation with different scale factors and modes."""
        for tens, scale_factor, mode, expected_shape in self.test_cases_3d:
            with self.subTest(scale_factor=scale_factor, mode=mode):
                result, = self.node.f(tens, scale_factor, mode)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result shape matches expected shape
                self.assertEqual(result.shape, expected_shape, f"Expected shape {expected_shape}, got {result.shape}")


    def test_interpolation_4d(self):
        """Test tensor interpolation with different scale factors and modes."""
        for tens, scale_factor, mode, expected_shape in self.test_cases_4d:
            with self.subTest(scale_factor=scale_factor, mode=mode):
                result, = self.node.f(tens, scale_factor, mode)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result shape matches expected shape
                self.assertEqual(result.shape, expected_shape, f"Expected shape {expected_shape}, got {result.shape}")

if __name__ == "__main__":
    unittest.main()
