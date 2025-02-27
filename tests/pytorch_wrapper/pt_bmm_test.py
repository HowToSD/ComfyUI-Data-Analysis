import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_bmm import PtBmm  # Updated import to PtBmm


class TestPtBmm(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtBmm()

        # Valid test cases: (Tensor A, Tensor B, Expected result)
        self.valid_test_cases = [
            # Case 1: Batch of 2 matrices (3x4) * (4x5) → (2, 3, 5)
            (torch.ones(2, 3, 4), torch.ones(2, 4, 5), torch.full((2, 3, 5), 4.0)),

            # Case 2: Batch of 3 matrices (2x3) * (3x2) → (3, 2, 2)
            (torch.tensor([[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]]), 
             torch.tensor([[[7.0, 8.0], [9.0, 10.0], [11.0, 12.0]]]), 
             torch.tensor([[[58.0, 64.0], [139.0, 154.0]]])),

            # Case 3: Identity matrix batch multiplication (should remain the same)
            (torch.eye(3).expand(4, -1, -1), torch.eye(3).expand(4, -1, -1), torch.eye(3).expand(4, -1, -1)),
        ]

        # Invalid test cases (should raise errors)
        self.invalid_test_cases = [
            (torch.ones(3, 4), torch.ones(4, 5)),  # 2D tensors (not allowed)
            (torch.ones(2, 3, 4), torch.ones(3, 4, 5)),  # Mismatched batch size
            (torch.ones(2, 3, 4, 5), torch.ones(2, 5, 6)),  # 4D tensors (not allowed)
            (torch.ones(2, 3, 4), torch.ones(2, 5, 6)),  # Matmul shape mismatch within batch
        ]

    def test_batched_matrix_multiplication(self):
        """Test valid batched matrix multiplication cases."""
        for tens_a, tens_b, expected in self.valid_test_cases:
            with self.subTest(tens_a=tens_a, tens_b=tens_b):
                result, = self.node.f(tens_a, tens_b)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected batch matrix multiplication
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

    def test_invalid_multiplication(self):
        """Test invalid cases where dimensions do not match."""
        for tens_a, tens_b in self.invalid_test_cases:
            with self.subTest(tens_a=tens_a, tens_b=tens_b):
                with self.assertRaises(Exception, msg=f"torch.bmm() should fail for shapes {tens_a.shape} and {tens_b.shape}"):
                    self.node.f(tens_a, tens_b)

if __name__ == "__main__":
    unittest.main()
