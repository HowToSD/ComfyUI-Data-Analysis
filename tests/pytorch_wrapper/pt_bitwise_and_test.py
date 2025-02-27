import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_bitwise_and import PtBitwiseAnd  # Updated import to PtBitwiseAnd


class TestPtBitwiseAnd(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtBitwiseAnd()

        # Test cases: (Tensor A, Tensor B, Expected result)
        self.test_cases = [
            (torch.tensor([0b0001, 0b0011, 0b0101]), torch.tensor([0b0001, 0b0010, 0b0110]), torch.tensor([0b0001, 0b0010, 0b0100])),
            (torch.tensor([0b1111, 0b1010, 0b1100]), torch.tensor([0b0101, 0b1100, 0b1010]), torch.tensor([0b0101, 0b1000, 0b1000])),
            (torch.tensor([1, 2, 3]), torch.tensor([3, 2, 1]), torch.tensor([1, 2, 1])),
            (torch.ones(2, 2, dtype=torch.int32), torch.zeros(2, 2, dtype=torch.int32), torch.zeros(2, 2, dtype=torch.int32)),
            (torch.full((2, 2), 0b1010, dtype=torch.int32), torch.full((2, 2), 0b1100, dtype=torch.int32), torch.full((2, 2), 0b1000, dtype=torch.int32)),
        ]

    def test_bitwise_and(self):
        """Test tensor element-wise bitwise AND using torch.bitwise_and()."""
        for tens_a, tens_b, expected in self.test_cases:
            with self.subTest(tens_a=tens_a, tens_b=tens_b):
                result, = self.node.f(tens_a, tens_b)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected bitwise AND operation
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
