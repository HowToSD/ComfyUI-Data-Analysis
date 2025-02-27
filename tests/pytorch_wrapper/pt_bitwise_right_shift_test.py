import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_bitwise_right_shift import PtBitwiseRightShift  # Updated import to PtBitwiseRightShift


class TestPtBitwiseRightShift(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtBitwiseRightShift()

        # Test cases: (Tensor A, Tensor B, Expected result)
        self.test_cases = [
            (torch.tensor([4, 8, 16], dtype=torch.int64), torch.tensor([1, 2, 3], dtype=torch.int64), torch.tensor([2, 2, 2], dtype=torch.int64)),  # 4>>1, 8>>2, 16>>3
            (torch.tensor([32, 64, 128], dtype=torch.int64), torch.tensor([2, 3, 4], dtype=torch.int64), torch.tensor([8, 8, 8], dtype=torch.int64)),  # 32>>2, 64>>3, 128>>4
            (torch.tensor([0b1000, 0b10000, 0b100000], dtype=torch.int64), torch.tensor([1, 2, 3], dtype=torch.int64), torch.tensor([0b0100, 0b00100, 0b000100], dtype=torch.int64)),  # Bitwise shift
            (torch.full((3, 3), 16, dtype=torch.int64), torch.full((3, 3), 2, dtype=torch.int64), torch.full((3, 3), 4, dtype=torch.int64)),  # 16>>2 = 4
            (torch.full((2, 2), 40, dtype=torch.int64), torch.full((2, 2), 3, dtype=torch.int64), torch.full((2, 2), 5, dtype=torch.int64)),  # 40>>3 = 5
        ]

    def test_bitwise_right_shift(self):
        """Test tensor element-wise bitwise right shift using torch.bitwise_right_shift()."""
        for tens_a, tens_b, expected in self.test_cases:
            with self.subTest(tens_a=tens_a, tens_b=tens_b):
                result, = self.node.f(tens_a, tens_b)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected bitwise right shift operation
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
