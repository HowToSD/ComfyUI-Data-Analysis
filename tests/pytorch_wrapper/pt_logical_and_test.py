import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_logical_and import PtLogicalAnd  # Updated import to PtLogicalAnd


class TestPtLogicalAnd(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtLogicalAnd()

        # Test cases: (Tensor A, Tensor B, Expected result)
        self.test_cases = [
            (torch.tensor([True, False, True]), torch.tensor([False, False, True]), torch.tensor([False, False, True])),
            (torch.tensor([[True, True], [False, False]]), torch.tensor([[True, False], [True, False]]), torch.tensor([[True, False], [False, False]])),
            (torch.ones(3, 3, dtype=torch.bool), torch.zeros(3, 3, dtype=torch.bool), torch.zeros(3, 3, dtype=torch.bool)),  # All true AND all false -> all false
            (torch.ones(2, 2, dtype=torch.bool), torch.ones(2, 2, dtype=torch.bool), torch.ones(2, 2, dtype=torch.bool)),  # All true AND all true -> all true
            (torch.tensor([1, 0, 1, 0], dtype=torch.bool), torch.tensor([1, 1, 0, 0], dtype=torch.bool), torch.tensor([True, False, False, False])),  # Mixed cases
        ]

    def test_logical_and(self):
        """Test tensor element-wise logical AND using torch.logical_and()."""
        for tens_a, tens_b, expected in self.test_cases:
            with self.subTest(tens_a=tens_a, tens_b=tens_b):
                result, = self.node.f(tens_a, tens_b)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected logical AND operation
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
