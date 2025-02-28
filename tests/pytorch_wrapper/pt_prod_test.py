import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_prod import PtProd


class TestPtProd(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtProd()

        # Test cases: (Tensor, Dim (as string), keepdim, Expected result)
        self.test_cases = [
            (
                torch.tensor([[1, 3, 2], [2, 1, 3]]),
                "0",
                False,
                torch.tensor([2, 3, 6])
            ),
            (
                torch.tensor([[1, 3, 2], [4, 0, 5]]),
                "1",
                True,
                torch.tensor([[6], [0]])
            ),
            (
                torch.tensor([[1, 3, 2], [4, 5, 6]]),
                "0",
                False,
                torch.tensor([4, 15, 12])
            ),
            (
                torch.tensor([[1, 3, 2], [4, 5, 6], [7, 8, 9]]),
                "1",
                False,
                torch.tensor([6, 120, 504])
            )
        ]

    def test_prod(self):
        """Test torch.prod behavior."""
        for tens, dim, keepdim, expected in self.test_cases:
            with self.subTest(tens=tens, dim=dim, keepdim=keepdim):
                result, = self.node.f(tens, dim, keepdim)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected product values
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
