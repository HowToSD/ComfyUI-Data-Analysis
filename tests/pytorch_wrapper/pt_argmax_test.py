import os
import sys
import unittest
import torch
import ast

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_argmax import PtArgmax


class TestPtArgmax(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtArgmax()

        # Test cases: (Tensor, Dim (as string), keepdim, Expected result)
        self.test_cases = [
            (torch.tensor([[1, 3, 2], [4, 0, 5]]), "0", False, torch.tensor([1, 0, 1])),
            (torch.tensor([[1, 3, 2], [4, 0, 5]]), "1", True, torch.tensor([[1], [2]])),
            (torch.tensor([[10, 3, 2], [123, 0, 5]]), "", False, torch.tensor(3)),
        ]

    def test_argmax(self):
        """Test torch.argmax behavior."""
        for tens, dim, keepdim, expected in self.test_cases:
            with self.subTest(tens=tens, dim=dim, keepdim=keepdim):
                result, = self.node.f(tens, dim, keepdim)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected indices
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
