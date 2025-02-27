import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_div import PtDiv  # Updated import to PtDiv


class TestPtDiv(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtDiv()

        # Test cases: (Tensor A, Tensor B, Expected result)
        self.test_cases = [
            (torch.tensor([4.0, 10.0, 18.0]), torch.tensor([2.0, 5.0, 6.0]), torch.tensor([2.0, 2.0, 3.0])),
            (torch.ones(3, 3), torch.ones(3, 3), torch.ones(3, 3)),  # 1 / 1 = 1
            (torch.full((2, 2), 4.0), torch.full((2, 2), 2.0), torch.full((2, 2), 2.0)),  # 4 / 2 = 2
            (torch.tensor([[6.0], [12.0]]), torch.tensor([[3.0], [4.0]]), torch.tensor([[2.0], [3.0]])),  # Element-wise division
        ]

    def test_division(self):
        """Test tensor division."""
        for tens_a, tens_b, expected in self.test_cases:
            with self.subTest(tens_a=tens_a, tens_b=tens_b):
                result, = self.node.f(tens_a, tens_b)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected quotient
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
