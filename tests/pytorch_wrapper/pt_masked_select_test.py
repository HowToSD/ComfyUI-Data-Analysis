import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_masked_select import PtMaskedSelect


class TestPtMaskedSelect(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtMaskedSelect()

        # Test cases: (Tensor, Masked Tensor, Expected result)
        self.test_cases = [
            (
                torch.tensor([[1, 2, 3], [40, 50, 60], [700, 800, 900]]),
                torch.tensor([[True, False, False], [False, True, False], [False, False, True]]),
                torch.tensor([1, 50, 900])
            ),
        ]

    def test_masked_select(self):
        """Test torch.masked_select behavior."""
        for tens, masked_tens, expected in self.test_cases:
            with self.subTest(tens=tens, masked_tens=masked_tens):
                result, = self.node.f(tens, masked_tens)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected selected values
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
