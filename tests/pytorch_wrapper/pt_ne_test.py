import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_ne import PtNe  # Updated import to PtNe


class TestPtNe(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtNe()

        # Test cases: (Tensor A, Tensor B, Expected result)
        self.test_cases = [
            (torch.tensor([1, 2, 3]), torch.tensor([1, 2, 3]), torch.tensor([False, False, False])),
            (torch.tensor([1, 2, 3]), torch.tensor([3, 2, 1]), torch.tensor([True, False, True])),
            (torch.ones(3, 3), torch.ones(3, 3), torch.full((3, 3), False, dtype=torch.bool)),
            (torch.zeros(2, 2), torch.ones(2, 2), torch.full((2, 2), True, dtype=torch.bool)),
            (torch.tensor([[1], [2]]), torch.tensor([[1], [3]]), torch.tensor([[False], [True]])),
        ]

    def test_inequality(self):
        """Test tensor element-wise inequality using torch.ne()."""
        for tens_a, tens_b, expected in self.test_cases:
            with self.subTest(tens_a=tens_a, tens_b=tens_b):
                result, = self.node.f(tens_a, tens_b)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected element-wise inequality
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
