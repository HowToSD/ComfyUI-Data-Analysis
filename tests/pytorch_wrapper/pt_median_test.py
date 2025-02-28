import os
import sys
import unittest
import torch
import ast

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_median import PtMedian


class TestPtMedian(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtMedian()

        # Test cases: (Tensor, Dim (as string), keepdim, Expected result)
        self.test_cases = [
            (
                torch.tensor([[1, 3, 2], [2, 1, 3], [4, 0, 5]]),
                "0",
                False,
                torch.tensor([2, 1, 3])
            ),
            (
                torch.tensor([[1, 3, 2], [4, 0, 5]]),
                "0",
                False,
                torch.tensor([1, 0, 2])  # Fix: torch.median returns the lower value when between two numbers
            ),
            (
                torch.tensor([[1, 3, 2], [4, 0, 5]]),
                "1",
                True,
                torch.tensor([[2], [4]])
            ),
            (
                torch.tensor([[1, 3, 2], [4, 0, 5], [7, 8, 6], [9, 2, 10]]),
                "0",
                False,
                torch.tensor([4, 2, 5])
            ),
            (
                torch.tensor([[1, 3, 2, 8], [4, 0, 5, 6], [7, 8, 6, 9]]),
                "1",
                False,
                torch.tensor([2, 4, 7])
            )
        ]

    def test_median(self):
        """Test torch.median behavior."""
        for tens, dim, keepdim, expected in self.test_cases:
            with self.subTest(tens=tens, dim=dim, keepdim=keepdim):
                result, = self.node.f(tens, dim, keepdim)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected median values
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
