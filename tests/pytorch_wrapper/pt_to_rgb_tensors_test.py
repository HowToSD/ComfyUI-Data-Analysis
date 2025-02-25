import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_to_rgb_tensors import PtToRgbTensors


class TestPtToRgbTensors(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtToRgbTensors()

        # Test cases: (Input tensor, Expected R, Expected G, Expected B)
        self.test_cases = [
            # 3D Tensor: [H, W, C]
            (
                torch.tensor([[[255, 128, 64], [0, 127, 255]]], dtype=torch.uint8),
                torch.tensor([[255, 0]], dtype=torch.uint8),
                torch.tensor([[128, 127]], dtype=torch.uint8),
                torch.tensor([[64, 255]], dtype=torch.uint8),
            ),

            # 4D Tensor: [B, H, W, C]
            (
                torch.tensor(
                    [[[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 255]]]], dtype=torch.uint8
                ),
                torch.tensor([[[255, 0], [0, 255]]], dtype=torch.uint8),
                torch.tensor([[[0, 255], [0, 255]]], dtype=torch.uint8),
                torch.tensor([[[0, 0], [255, 255]]], dtype=torch.uint8),
            ),
        ]

    def test_split_rgb(self):
        """Test splitting RGB tensors correctly."""
        for tensor, expected_r, expected_g, expected_b in self.test_cases:
            with self.subTest(tensor_shape=tensor.shape):
                r, g, b = self.node.f(tensor)

                # Ensure return values are tensors
                self.assertTrue(isinstance(r, torch.Tensor), "R is not a tensor")
                self.assertTrue(isinstance(g, torch.Tensor), "G is not a tensor")
                self.assertTrue(isinstance(b, torch.Tensor), "B is not a tensor")

                # Ensure shapes match
                self.assertEqual(r.shape, expected_r.shape, f"R shape mismatch: expected {expected_r.shape}, got {r.shape}")
                self.assertEqual(g.shape, expected_g.shape, f"G shape mismatch: expected {expected_g.shape}, got {g.shape}")
                self.assertEqual(b.shape, expected_b.shape, f"B shape mismatch: expected {expected_b.shape}, got {b.shape}")

                # Ensure values match
                torch.testing.assert_close(r, expected_r, msg="R values mismatch")
                torch.testing.assert_close(g, expected_g, msg="G values mismatch")
                torch.testing.assert_close(b, expected_b, msg="B values mismatch")

    def test_invalid_input(self):
        """Test error handling for non-3-channel input."""
        invalid_tensor = torch.rand(1, 512, 512, 4)  # 4 channels instead of 3
        with self.assertRaises(ValueError) as context:
            self.node.f(invalid_tensor)
        self.assertIn("Expected a 3-channel tensor", str(context.exception))


if __name__ == "__main__":
    unittest.main()
