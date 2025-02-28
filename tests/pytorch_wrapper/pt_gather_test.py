import os
import sys
import unittest
import torch
import ast

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_gather import PtGather


class TestPtGather(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtGather()

        # Test cases: (Tensor, Dim, Index (as string), Expected result)
        self.test_cases = [
            (
                torch.tensor([[10, 20, 30, 40, 50], [100, 200, 300, 400, 500]]),
                1,
                "[[0, 4, 3, 2, 0], [4, 3, 0, 0, 0]]",
                torch.tensor([[10, 50, 40, 30, 10], [500, 400, 100, 100, 100]])
            ),
            (
                torch.tensor([[1, 2], [3, 4]]),
                0,
                "[[1, 0], [0, 1]]",
                torch.tensor([[3, 2], [1, 4]])
            ),
        ]

    def test_gather(self):
        """Test torch.gather behavior."""
        for tens, dim, index, expected in self.test_cases:
            with self.subTest(tens=tens, dim=dim, index=index):
                result, = self.node.f(tens, dim, index)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected gathered values
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
