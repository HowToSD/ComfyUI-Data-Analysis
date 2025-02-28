import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_where import PtWhere


class TestPtWhere(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtWhere()

        # Test cases: (Condition Tensor, True Tensor, False Tensor, Expected Output)
        self.test_cases = [
            (
                torch.tensor([[True, False], [False, True]]),
                torch.tensor([[1, 2], [3, 4]]),
                torch.tensor([[5, 6], [7, 8]]),
                torch.tensor([[1, 6], [7, 4]])
            ),
            (
                torch.tensor([True, False, True]),
                torch.tensor([10, 20, 30]),
                torch.tensor([100, 200, 300]),
                torch.tensor([10, 200, 30])
            ),
            (
                torch.tensor([[False, False], [True, True]]),
                torch.tensor([[1.5, 2.5], [3.5, 4.5]]),
                torch.tensor([[5.5, 6.5], [7.5, 8.5]]),
                torch.tensor([[5.5, 6.5], [3.5, 4.5]])
            ),
            (
                torch.tensor([[[True, False], [False, True]], [[False, True], [True, False]]]),
                torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]),
                torch.tensor([[[9, 10], [11, 12]], [[13, 14], [15, 16]]]),
                torch.tensor([[[1, 10], [11, 4]], [[13, 6], [7, 16]]])
            ),
        ]

    def test_where(self):
        """Test torch.where behavior."""
        for condition_tens, true_tens, false_tens, expected in self.test_cases:
            with self.subTest(condition_tens=condition_tens, true_tens=true_tens, false_tens=false_tens):
                result, = self.node.f(condition_tens, true_tens, false_tens)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected values
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
