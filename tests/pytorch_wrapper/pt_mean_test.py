import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_mean import PtMean


class TestPtMean(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtMean()

        # Test cases: (Tensor, Dim (as string), keepdim, Expected result)
        self.test_cases = [
            # Float tensor cases
            (
                torch.tensor([[1.0, 3.0, 2.0], [4.0, 0.0, 5.0]], dtype=torch.float),
                "0",
                False,
                torch.tensor([2.5, 1.5, 3.5], dtype=torch.float)
            ),
            (
                torch.tensor([[1.0, 3.0, 2.0], [4.0, 0.0, 5.0]], dtype=torch.float),
                "1",
                True,
                torch.tensor([[2.], [3.]], dtype=torch.float)
            ),
            (
                torch.tensor([[[1.0, 5.0], [2.0, 8.0]], [[3.0, 4.0], [6.0, 7.0]]], dtype=torch.float),
                "(0, 1)",
                False,
                torch.tensor([3.0, 6.0], dtype=torch.float)
            ),
            (
                # Reduce across all axes
                torch.tensor([[1.0, 3.0, 2.0], [4.0, 0.0, 5.0]], dtype=torch.float),
                "",  # Passing empty string to reduce across all dimensions
                False,
                torch.tensor(2.5, dtype=torch.float)
            ),
            # Complex tensor cases
            (
                torch.tensor([[1 + 1j, 3 + 3j, 2 + 2j], [4 + 4j, 0 + 0j, 5 + 5j]], dtype=torch.complex64),
                "0",
                False,
                torch.tensor([2.5 + 2.5j, 1.5 + 1.5j, 3.5 + 3.5j], dtype=torch.complex64)
            ),
            (
                torch.tensor([[1 + 1j, 3 + 3j, 2 + 2j], [4 + 4j, 0 + 0j, 5 + 5j]], dtype=torch.complex64),
                "1",
                True,
                torch.tensor([[2. + 2j], [3. + 3j]], dtype=torch.complex64)
            ),
            (
                torch.tensor([[[1 + 1j, 5 + 5j], [2 + 2j, 8 + 8j]], [[3 + 3j, 4 + 4j], [6 + 6j, 7 + 7j]]], dtype=torch.complex64),
                "(0, 1)",
                False,
                torch.tensor([3. + 3j, 6. + 6j], dtype=torch.complex64)
            ),
            (
                # Reduce across all axes
                torch.tensor([[1 + 1j, 3 + 3j, 2 + 2j], [4 + 4j, 0 + 0j, 5 + 5j]], dtype=torch.complex64),
                "",  # Passing empty string to reduce across all dimensions
                False,
                torch.tensor(2.5 + 2.5j, dtype=torch.complex64)
            )
        ]

    def test_mean(self):
        """Test torch.mean behavior."""
        for tens, dim, keepdim, expected in self.test_cases:
            with self.subTest(tens=tens, dim=dim, keepdim=keepdim):
                result, = self.node.f(tens, dim, keepdim)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected mean values
                self.assertTrue(torch.allclose(result, expected), f"Expected {expected}, got {result}")

if __name__ == "__main__":
    unittest.main()
