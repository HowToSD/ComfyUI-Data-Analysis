import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_exp import PtExp  # Updated import to PtExp


class TestPtExp(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtExp()

        # Test cases: (Tensor A, Expected result)
        self.test_cases = [
            (torch.tensor([0.0, 1.0, 2.0], dtype=torch.float32), torch.exp(torch.tensor([0.0, 1.0, 2.0], dtype=torch.float32))),  # Edge cases
            (torch.tensor([-1.0, -2.0, 0.5], dtype=torch.float32), torch.exp(torch.tensor([-1.0, -2.0, 0.5], dtype=torch.float32))),  # Common values
            (torch.tensor([[0.1, -0.3], [0.7, -0.9]], dtype=torch.float32), torch.exp(torch.tensor([[0.1, -0.3], [0.7, -0.9]], dtype=torch.float32))),  # 2D case
            (torch.full((2, 2), 0.6, dtype=torch.float32), torch.exp(torch.full((2, 2), 0.6, dtype=torch.float32))),  # Constant matrix
        ]

    def test_exp(self):
        """Test tensor element-wise exponential function using torch.exp()."""
        for tens_a, expected in self.test_cases:
            with self.subTest(tens_a=tens_a):
                result, = self.node.f(tens_a)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected exp values
                self.assertTrue(torch.allclose(result, expected, atol=1e-6), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
