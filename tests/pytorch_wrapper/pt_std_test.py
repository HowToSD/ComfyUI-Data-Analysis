import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_std import PtStd


class TestPtStd(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtStd()

        # Define test cases with string-based dimensions
        self.test_cases = [
            # Sample standard deviation (Bessel's correction) along dim=0
            (
                torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]),
                "0",
                1,
                False,
                torch.std(torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]), dim=0, correction=1, keepdim=False)
            ),
            # Sample standard deviation along dim=1, with keepdim=True
            (
                torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]),
                "1",
                1,
                True,
                torch.std(torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]), dim=1, correction=1, keepdim=True)
            ),
            # Sample standard deviation across both axes (dim=(0,1))
            (
                torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]),
                "(0, 1)",
                1,
                False,
                torch.std(torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]), dim=(0, 1), correction=1, keepdim=False)
            ),
            # Sample standard deviation across all elements (dim=None) - Entire tensor
            (
                torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]),
                "",
                1,
                False,
                torch.std(torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]), correction=1, keepdim=False)
            ),
            # Population standard deviation along dim=0 (correction=0)
            (
                torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]),
                "0",
                0,
                False,
                torch.std(torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]), dim=0, correction=0, keepdim=False)
            ),
            # Population standard deviation along dim=1 with keepdim=True (correction=0)
            (
                torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]),
                "1",
                0,
                True,
                torch.std(torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]), dim=1, correction=0, keepdim=True)
            )
        ]

    def test_std(self):
        """Test torch.std behavior."""
        for tens, dim, correction, keepdim, expected in self.test_cases:
            with self.subTest(tens=tens, dim=dim, correction=correction, keepdim=keepdim):
                result, = self.node.f(tens, dim, correction, keepdim)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected standard deviation values
                self.assertTrue(torch.allclose(result, expected, atol=1e-6), f"Expected {expected}, got {result}")


if __name__ == "__main__":
    unittest.main()
