import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_bitwise_not import PtBitwiseNot  # Updated import to PtBitwiseNot


class TestPtBitwiseNot(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtBitwiseNot()

        # Test cases: (Tensor A, Expected result)
        self.test_cases = [
            (torch.tensor([0, 1, 2, 3], dtype=torch.int32), torch.tensor([-1, -2, -3, -4], dtype=torch.int32)),  # Bitwise NOT
            (torch.tensor([0b0000, 0b0001, 0b0010], dtype=torch.int32), torch.tensor([-1, -2, -3], dtype=torch.int32)),  # Binary representation
            (torch.tensor([[5, 10], [15, 20]], dtype=torch.int32), torch.tensor([[-6, -11], [-16, -21]], dtype=torch.int32)),  # Matrix case
            (torch.full((2, 2), 0, dtype=torch.int32), torch.full((2, 2), -1, dtype=torch.int32)),  # NOT 0 -> -1
            (torch.full((3, 3), -1, dtype=torch.int32), torch.full((3, 3), 0, dtype=torch.int32)),  # NOT -1 -> 0
        ]

    def test_bitwise_not(self):
        """Test tensor element-wise bitwise NOT using torch.bitwise_not()."""
        for tens_a, expected in self.test_cases:
            with self.subTest(tens_a=tens_a):
                result, = self.node.f(tens_a)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected bitwise NOT operation
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
