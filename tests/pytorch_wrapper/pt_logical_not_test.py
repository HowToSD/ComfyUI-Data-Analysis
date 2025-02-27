import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_logical_not import PtLogicalNot  # Updated import to PtLogicalNot


class TestPtLogicalNot(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtLogicalNot()

        # Test cases: (Tensor A, Expected result)
        self.test_cases = [
            (torch.tensor([True, False, True]), torch.tensor([False, True, False])),
            (torch.tensor([[True, True], [False, False]]), torch.tensor([[False, False], [True, True]])),
            (torch.ones(3, 3, dtype=torch.bool), torch.zeros(3, 3, dtype=torch.bool)),  # NOT all true -> all false
            (torch.zeros(2, 2, dtype=torch.bool), torch.ones(2, 2, dtype=torch.bool)),  # NOT all false -> all true
            (torch.tensor([1, 0, 1, 0], dtype=torch.bool), torch.tensor([False, True, False, True])),  # Mixed cases
        ]

    def test_logical_not(self):
        """Test tensor element-wise logical NOT using torch.logical_not()."""
        for tens_a, expected in self.test_cases:
            with self.subTest(tens_a=tens_a):
                result, = self.node.f(tens_a)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected logical NOT operation
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
