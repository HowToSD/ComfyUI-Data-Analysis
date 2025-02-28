import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_sum import PtSum


class TestPtSum(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtSum()

        # Test cases: (Tensor, Dim (as string), keepdim, Expected result)
        self.test_cases = [
            (
                torch.tensor([[1, 3, 2], [2, 1, 3]]),
                "0",
                False,
                torch.tensor([3, 4, 5])
            ),
            (
                torch.tensor([[1, 3, 2], [4, 0, 5]]),
                "1",
                True,
                torch.tensor([[6], [9]])
            ),
            (
                torch.tensor([[1, 3, 2], [4, 5, 6]]),
                "0",
                False,
                torch.tensor([5, 8, 8])
            ),
            (
                torch.tensor([[1, 3, 2], [4, 5, 6], [7, 8, 9]]),
                "1",
                False,
                torch.tensor([6, 15, 24])
            ),
            (
                torch.tensor([[1, 2], [3, 4]]),
                "",
                False,
                torch.tensor(10)  # Sum of all elements
            ),
            (
                torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]),
                "(0, 1)",
                False,
                torch.tensor([16, 20])  # Sum over dimensions (0, 1)
            )
        ]

    def test_sum(self):
        """Test torch.sum behavior."""
        for tens, dim, keepdim, expected in self.test_cases:
            with self.subTest(tens=tens, dim=dim, keepdim=keepdim):
                result, = self.node.f(tens, dim, keepdim)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected sum values
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
