import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_flatten import PtFlatten


class TestPtFlatten(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtFlatten()

        # Test cases: (Input tensor, Expected flattened tensor shape)
        self.test_cases = [
            (torch.randn(3, 4, 5), (60,)),  # 3D Tensor
            (torch.randn(2, 3, 4, 5), (120,)),  # 4D Tensor
            (torch.randn(10, 10), (100,)),  # 2D Tensor
            (torch.randn(1), (1,)),  # 1D Tensor remains unchanged
        ]

    def test_flatten(self):
        """Test flattening tensors correctly."""
        for tensor, expected_shape in self.test_cases:
            with self.subTest(tensor_shape=tensor.shape):
                flattened, = self.node.f(tensor)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(flattened, torch.Tensor), "Output is not a tensor")

                # Ensure shape matches expected flattened shape
                self.assertEqual(flattened.shape, expected_shape, f"Shape mismatch: expected {expected_shape}, got {flattened.shape}")

if __name__ == "__main__":
    unittest.main()
