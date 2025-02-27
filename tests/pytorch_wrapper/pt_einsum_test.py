import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_einsum import PtEinsum  # Updated import to PtEinsum


class TestPtEinsum(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtEinsum()

    def test_trace_extraction(self):
        """Extract the diagonal (1,2,3,4,5) and sum it up (trace)."""
        matrix = torch.tensor([[1, 0, 0, 0, 0],
                               [0, 2, 0, 0, 0],
                               [0, 0, 3, 0, 0],
                               [0, 0, 0, 4, 0],
                               [0, 0, 0, 0, 5]], dtype=torch.float32)
        expected = torch.tensor(15.0)  # Sum of diagonal
        result, = self.node.f("ii", matrix)  # Only requires `tens_a`
        self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

    def test_diagonal_extraction(self):
        """Extract diagonal elements (1,2,3,4,5)."""
        matrix = torch.tensor([[1, 0, 0, 0, 0],
                               [0, 2, 0, 0, 0],
                               [0, 0, 3, 0, 0],
                               [0, 0, 0, 4, 0],
                               [0, 0, 0, 0, 5]], dtype=torch.float32)
        expected = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)
        result, = self.node.f("ii->i", matrix)  # Only requires `tens_a`
        self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

    def test_hadamard_product(self):
        """Compute Hadamard product (element-wise multiplication)."""
        a = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.float32)
        b = torch.tensor([[9, 10, 11, 12], [13, 14, 15, 16]], dtype=torch.float32)
        expected = a * b
        result, = self.node.f("ij,ij->ij", a, b)
        self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

    def test_matrix_multiplication(self):
        """Test standard matrix multiplication."""
        a = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.float32)
        b = torch.tensor([[9, 10], [11, 12], [13, 14], [15, 16]], dtype=torch.float32)
        expected = torch.mm(a, b)
        result, = self.node.f("ij,jk->ik", a, b)
        self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

    def test_3d_tensor_multiplication(self):
        """Test matrix multiplication for rank-3 tensors."""
        a = torch.ones(2, 3, 4, dtype=torch.float32)
        b = torch.ones(2, 4, 5, dtype=torch.float32)
        expected = torch.matmul(a, b)
        result, = self.node.f("bij,bjk->bik", a, b)
        self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

    def test_4d_tensor_multiplication(self):
        """Test matrix multiplication for rank-4 tensors."""
        a = torch.ones(2, 3, 4, 6, dtype=torch.float32)  # (batch, groups, rows, cols)
        b = torch.ones(2, 3, 6, 5, dtype=torch.float32)  # (batch, groups, cols, out_features)

        expected = torch.matmul(a, b)  # Standard 4D matrix multiplication
        result, = self.node.f("bijk,bikl->bijl", a, b)  # Correct einsum notation

        self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

    def test_bilinear_transformation(self):
        """Test bilinear transformation: a vector, W matrix, and b vector."""
        a = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)
        W = torch.tensor([[6, 7, 8, 9, 10],
                          [11, 12, 13, 14, 15],
                          [16, 17, 18, 19, 20],
                          [21, 22, 23, 24, 25],
                          [26, 27, 28, 29, 30]], dtype=torch.float32)
        b = torch.tensor([31, 32, 33, 34, 35], dtype=torch.float32)

        expected = torch.dot(a, torch.matmul(W, b))
        result, = self.node.f("i,ij,j->", a, W, b)
        self.assertTrue(torch.equal(result, expected), f"Expected {expected}, got {result}")

    def test_tensor_format_conversion(self):
        """Test conversion from (B, C, H, W) format to (B, H, W, C) format."""
        a = torch.randn(2, 3, 64, 64, dtype=torch.float32)  # (Batch, Channels, Height, Width)

        expected = a.permute(0, 2, 3, 1)  # Convert to (Batch, Height, Width, Channels)
        result, = self.node.f("bchw->bhwc", a)  # Correct einsum notation for format swap

        self.assertTrue(torch.equal(result, expected), f"Expected {expected.shape}, got {result.shape}")


if __name__ == "__main__":
    unittest.main()
