import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_tan import PtTan  # Updated import to PtTan


class TestPtTan(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtTan()

        # Test cases: (Tensor A, Expected result)
        self.test_cases = [
            (torch.tensor([0.0, torch.pi / 4, -torch.pi / 4], dtype=torch.float32), torch.tan(torch.tensor([0.0, torch.pi / 4, -torch.pi / 4], dtype=torch.float32))),  # Common angles
            (torch.tensor([0.5, -0.5], dtype=torch.float32), torch.tan(torch.tensor([0.5, -0.5], dtype=torch.float32))),  # General values
            (torch.tensor([[0.1, -0.3], [0.7, -0.9]], dtype=torch.float32), torch.tan(torch.tensor([[0.1, -0.3], [0.7, -0.9]], dtype=torch.float32))),  # 2D case
            (torch.full((2, 2), 0.6, dtype=torch.float32), torch.tan(torch.full((2, 2), 0.6, dtype=torch.float32))),  # Constant matrix
        ]

    def test_tan(self):
        """Test tensor element-wise tangent using torch.tan()."""
        for tens_a, expected in self.test_cases:
            with self.subTest(tens_a=tens_a):
                result, = self.node.f(tens_a)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected tan values
                self.assertTrue(torch.allclose(result, expected, atol=1e-6), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
