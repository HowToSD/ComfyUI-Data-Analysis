import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_mm import PtMm  # Updated import to PtMm


class TestPtMm(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtMm()

        # Valid test cases: (Tensor A, Tensor B, Expected result)
        self.valid_test_cases = [
            # Case 1: 2D x 2D (matrix-matrix multiplication)
            (torch.tensor([[1.0, 2.0], [3.0, 4.0]]), torch.tensor([[5.0, 6.0], [7.0, 8.0]]), torch.tensor([[19.0, 22.0], [43.0, 50.0]])),

            # Case 2: 2D identity matrix multiplication (should remain the same)
            (torch.eye(3), torch.eye(3), torch.eye(3)),

            # Case 3: Rectangular 2D matrix multiplication
            (torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]), torch.tensor([[7.0, 8.0], [9.0, 10.0], [11.0, 12.0]]), torch.tensor([[58.0, 64.0], [139.0, 154.0]])),
        ]

        # Invalid test cases (should raise errors)
        self.invalid_test_cases = [
            (torch.tensor([1.0, 2.0, 3.0]), torch.tensor([4.0, 5.0, 6.0])),  # 1D x 1D (dot product not supported by mm)
            (torch.tensor([[1.0, 2.0]]), torch.tensor([3.0, 4.0])),  # 2D x 1D mismatch
            (torch.ones(2, 3, 4), torch.ones(4, 5)),  # 3D x 2D is invalid for mm
            (torch.ones(2, 3, 4), torch.ones(2, 4, 5)),  # 3D x 3D is invalid for mm
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
                with self.assertRaises(ValueError, msg=f"torch.mm() should fail for shapes {tens_a.shape} and {tens_b.shape}"):
                    self.node.f(tens_a, tens_b)

if __name__ == "__main__":
    unittest.main()
