import os
import sys
import unittest
import torch
import ast

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_scatter import PtScatter


class TestPtScatter(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtScatter()

        # Test cases: (Target Tensor, Dim, Index Tensor (as string), Source Tensor (as string), Expected Output)
        self.test_cases = [
            (
                torch.tensor([
                    [10, 11, 12],
                    [21, 22, 23],
                    [31, 32, 33],
                ]),
                0,
                "[[0, 1, 0], [1, 1, 2]]",
                "[[2, 4, 6], [4, 4, 2]]",
                torch.tensor([
                    [2, 11, 6],
                    [4, 4, 23],
                    [31, 32, 2],
                ])
            )
        ]

    def test_scatter(self):
        """Test torch.scatter behavior."""
        for tens, dim, index, src, expected in self.test_cases:
            with self.subTest(tens=tens, dim=dim, index=index, src=src):
                result, = self.node.f(tens, dim, index, src)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected values
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
