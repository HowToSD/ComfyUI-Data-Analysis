import os
import sys
import unittest
import torch
import ast

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_index_select import PtIndexSelect


class TestPtIndexSelect(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtIndexSelect()

        # Test cases: (Tensor, Dim, Index (as string), Expected result)
        self.test_cases = [
            (
                torch.tensor([[1, 2, 3], [40, 50, 60], [700, 800, 900]]),
                0,
                "[0, 2]",
                torch.tensor([[1, 2, 3], [700, 800, 900]])
            ),
            (
                torch.tensor([[1, 2, 3], [40, 50, 60], [700, 800, 900]]),
                1,
                "[1, 2]",
                torch.tensor([[2, 3], [50, 60], [800, 900]])
            ),
        ]

    def test_index_select(self):
        """Test torch.index_select behavior."""
        for tens, dim, index, expected in self.test_cases:
            with self.subTest(tens=tens, dim=dim, index=index):
                result, = self.node.f(tens, dim, index)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected selected values
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
