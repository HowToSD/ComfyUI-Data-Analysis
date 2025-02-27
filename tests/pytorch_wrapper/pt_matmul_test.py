import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_matmul import PtMatMul  # Updated import to PtMatMul


class TestPtMatMul(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtMatMul()

        # Valid test cases: (Tensor A, Tensor B, Expected result)
        self.valid_test_cases = [
            # Case 1: 1D x 1D (dot product)
            (torch.tensor([1.0, 2.0, 3.0]), torch.tensor([4.0, 5.0, 6.0]), torch.tensor(32.0)),

            # Case 2: 1D x 2D (vector-matrix multiplication)
            (torch.tensor([1.0, 2.0]), torch.tensor([[3.0, 4.0], [5.0, 6.0]]), torch.tensor([13.0, 16.0])),

            # Case 3: 2D x 2D (matrix-matrix multiplication)
            (torch.tensor([[1.0, 2.0], [3.0, 4.0]]), torch.tensor([[5.0, 6.0], [7.0, 8.0]]), torch.tensor([[19.0, 22.0], [43.0, 50.0]])),

            # Case 4: 3D x 2D (batched matrix-matrix multiplication)
            (torch.ones(2, 3, 4), torch.ones(4, 5), torch.full((2, 3, 5), 4.0)),  # (2,3,4) * (4,5) → (2,3,5)

            # Case 5: 3D x 3D (batched matrix multiplication with broadcasting)
            (torch.ones(2, 3, 4), torch.ones(2, 4, 5), torch.full((2, 3, 5), 4.0)),  # (2,3,4) * (2,4,5) → (2,3,5)
        ]

        # Invalid test cases (should raise errors)
        self.invalid_test_cases = [
            (torch.ones(2, 3), torch.ones(4, 2)),  # (2,3) * (4,2) is invalid
            (torch.tensor([1.0, 2.0, 3.0]), torch.tensor([4.0, 5.0])),  # Vector size mismatch
            (torch.ones(2, 3, 4), torch.ones(3, 5)),  # (2,3,4) * (3,5) should fail due to misalignment
        ]

    def test_matrix_multiplication(self):
        """Test valid matrix multiplication cases."""
        for tens_a, tens_b, expected in self.valid_test_cases:
            with self.subTest(tens_a=tens_a, tens_b=tens_b):
                result, = self.node.f(tens_a, tens_b)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result matches expected matrix multiplication
                self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

    def test_invalid_multiplication(self):
        """Test invalid cases where dimensions do not match."""
        for tens_a, tens_b in self.invalid_test_cases:
            with self.subTest(tens_a=tens_a, tens_b=tens_b):
                with self.assertRaises(RuntimeError, msg=f"MatMul should fail for shapes {tens_a.shape} and {tens_b.shape}"):
                    self.node.f(tens_a, tens_b)

if __name__ == "__main__":
    unittest.main()
