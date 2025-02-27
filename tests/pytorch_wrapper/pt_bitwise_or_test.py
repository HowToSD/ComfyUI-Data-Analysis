import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_bitwise_or import PtBitwiseOr  # Updated import to PtBitwiseOr


class TestPtBitwiseOr(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtBitwiseOr()

        # Test cases: (Tensor A, Tensor B, Expected result)
        self.test_cases = [
            (torch.tensor([0b0001, 0b0011, 0b0101], dtype=torch.int32),
             torch.tensor([0b0010, 0b0100, 0b0110], dtype=torch.int32),
             torch.tensor([0b0011, 0b0111, 0b0111], dtype=torch.int32)),  # Binary OR
            
            (torch.tensor([1, 2, 4], dtype=torch.int32),
             torch.tensor([8, 16, 32], dtype=torch.int32),
             torch.tensor([9, 18, 36], dtype=torch.int32)),  # Decimal OR
            
            (torch.tensor([5, 10, 15], dtype=torch.int32),
             torch.tensor([3, 6, 12], dtype=torch.int32),
             torch.tensor([7, 14, 15], dtype=torch.int32)),  # Mixed values
            
            (torch.zeros(3, 3, dtype=torch.int32),
             torch.ones(3, 3, dtype=torch.int32),
             torch.ones(3, 3, dtype=torch.int32)),  # OR with all ones
            
            (torch.full((2, 2), 0b1010, dtype=torch.int32),
             torch.full((2, 2), 0b1100, dtype=torch.int32),
             torch.full((2, 2), 0b1110, dtype=torch.int32)),  # OR with constant matrices
        ]

    def test_bitwise_or(self):
        """Test tensor element-wise bitwise OR using torch.bitwise_or()."""
        for tens_a, tens_b, expected in self.test_cases:
            with self.subTest(tens_a=tens_a, tens_b=tens_b):
                result, = self.node.f(tens_a, tens_b)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected bitwise OR operation
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
