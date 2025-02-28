import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_sqrt import PtSqrt  # Updated import to PtSqrt


class TestPtSqrt(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtSqrt()

        # Test cases: (Tensor A, Expected result)
        self.test_cases = [
            (torch.tensor([1.0, 4.0, 9.0], dtype=torch.float32), torch.sqrt(torch.tensor([1.0, 4.0, 9.0], dtype=torch.float32))),  # Perfect squares
            (torch.tensor([0.5, 2.0, 3.0], dtype=torch.float32), torch.sqrt(torch.tensor([0.5, 2.0, 3.0], dtype=torch.float32))),  # Common values
            (torch.tensor([[1.5, 3.2], [4.7, 5.9]], dtype=torch.float32), torch.sqrt(torch.tensor([[1.5, 3.2], [4.7, 5.9]], dtype=torch.float32))),  # 2D case
            (torch.full((2, 2), 2.5, dtype=torch.float32), torch.sqrt(torch.full((2, 2), 2.5, dtype=torch.float32))),  # Constant matrix
        ]

    def test_sqrt(self):
        """Test tensor element-wise square root using torch.sqrt()."""
        for tens_a, expected in self.test_cases:
            with self.subTest(tens_a=tens_a):
                result, = self.node.f(tens_a)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected sqrt values
                self.assertTrue(torch.allclose(result, expected, atol=1e-6), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
