import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_neg import PtNeg  # Updated import to PtNeg


class TestPtNeg(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtNeg()

        # Test cases: (Tensor A, Expected result)
        self.test_cases = [
            (torch.tensor([1, -2, 3]), torch.tensor([-1, 2, -3])),
            (torch.tensor([0, 5, -7]), torch.tensor([0, -5, 7])),
            (torch.ones(3, 3), torch.full((3, 3), -1.0)),  # Negation of ones
            (torch.zeros(2, 2), torch.zeros(2, 2)),  # Negation of zeros
            (torch.tensor([[5], [-10]]), torch.tensor([[-5], [10]])),  # Column vector case
        ]

    def test_neg(self):
        """Test tensor element-wise negation using torch.neg()."""
        for tens_a, expected in self.test_cases:
            with self.subTest(tens_a=tens_a):
                result, = self.node.f(tens_a)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected negation
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
