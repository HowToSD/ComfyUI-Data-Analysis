import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_add import PtAdd


class TestPtAdd(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtAdd()

        # Test cases: (Tensor A, Tensor B, Expected result)
        self.test_cases = [
            (torch.tensor([1.0, 2.0, 3.0]), torch.tensor([4.0, 5.0, 6.0]), torch.tensor([5.0, 7.0, 9.0])),
            (torch.ones(3, 3), torch.ones(3, 3), torch.full((3, 3), 2.0)),
            (torch.zeros(2, 2), torch.ones(2, 2), torch.ones(2, 2)),
            (torch.tensor([[1.0], [2.0]]), torch.tensor([[3.0], [4.0]]), torch.tensor([[4.0], [6.0]])),
        ]

    def test_addition(self):
        """Test tensor addition."""
        for tens_a, tens_b, expected in self.test_cases:
            with self.subTest(tens_a=tens_a, tens_b=tens_b):
                result, = self.node.f(tens_a, tens_b)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected sum
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
