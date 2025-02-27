import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_bitwise_left_shift import PtBitwiseLeftShift  # Updated import to PtBitwiseLeftShift


class TestPtBitwiseLeftShift(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtBitwiseLeftShift()

        # Test cases: (Tensor A, Tensor B, Expected result)
        self.test_cases = [
            (torch.tensor([1, 2, 4], dtype=torch.int64), torch.tensor([1, 2, 3], dtype=torch.int64), torch.tensor([2, 8, 32], dtype=torch.int64)),  # 1<<1, 2<<2, 4<<3
            (torch.tensor([4, 8, 16], dtype=torch.int64), torch.tensor([2, 1, 3], dtype=torch.int64), torch.tensor([16, 16, 128], dtype=torch.int64)),  # 4<<2, 8<<1, 16<<3
            (torch.tensor([0b0001, 0b0010, 0b0100], dtype=torch.int64), torch.tensor([1, 2, 3], dtype=torch.int64), torch.tensor([0b0010, 0b1000, 0b100000], dtype=torch.int64)),  # Bitwise shift
            (torch.ones(3, 3, dtype=torch.int64), torch.full((3, 3), 2, dtype=torch.int64), torch.full((3, 3), 4, dtype=torch.int64)),  # 1<<2 = 4
            (torch.full((2, 2), 5, dtype=torch.int64), torch.full((2, 2), 3, dtype=torch.int64), torch.full((2, 2), 40, dtype=torch.int64)),  # 5<<3 = 40
        ]

    def test_bitwise_left_shift(self):
        """Test tensor element-wise bitwise left shift using torch.bitwise_left_shift()."""
        for tens_a, tens_b, expected in self.test_cases:
            with self.subTest(tens_a=tens_a, tens_b=tens_b):
                result, = self.node.f(tens_a, tens_b)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected bitwise left shift operation
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
