import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_logical_or import PtLogicalOr  # Updated import to PtLogicalOr


class TestPtLogicalOr(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtLogicalOr()

        # Test cases: (Tensor A, Tensor B, Expected result)
        self.test_cases = [
            (torch.tensor([True, False, True]), torch.tensor([False, False, True]), torch.tensor([True, False, True])),
            (torch.tensor([[True, True], [False, False]]), torch.tensor([[False, True], [True, False]]), torch.tensor([[True, True], [True, False]])),
            (torch.ones(3, 3, dtype=torch.bool), torch.zeros(3, 3, dtype=torch.bool), torch.ones(3, 3, dtype=torch.bool)),  # All true OR all false -> all true
            (torch.zeros(2, 2, dtype=torch.bool), torch.zeros(2, 2, dtype=torch.bool), torch.zeros(2, 2, dtype=torch.bool)),  # All false OR all false -> all false
            (torch.tensor([1, 0, 1, 0], dtype=torch.bool), torch.tensor([1, 1, 0, 0], dtype=torch.bool), torch.tensor([True, True, True, False])),  # Mixed cases
        ]

    def test_logical_or(self):
        """Test tensor element-wise logical OR using torch.logical_or()."""
        for tens_a, tens_b, expected in self.test_cases:
            with self.subTest(tens_a=tens_a, tens_b=tens_b):
                result, = self.node.f(tens_a, tens_b)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected logical OR operation
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
