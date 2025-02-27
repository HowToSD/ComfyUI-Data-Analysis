import os
import sys
import unittest
import torch


PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_squeeze import PtSqueeze  # Importing the PtSqueeze class


class TestPtSqueeze(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtSqueeze()

        # Define test cases: (input_tensor, dim, expected_shape)
        self.test_cases = [
            # Case 1: Squeezing a singleton dimension
            (torch.ones(1, 3, 4), 0, (3, 4)),  # (1,3,4) -> (3,4)
            (torch.ones(2, 1, 4), 1, (2, 4)),  # (2,1,4) -> (2,4)

            # Case 2: No change if dim is not a singleton
            (torch.ones(2, 3, 4), 1, (2, 3, 4)),  # (2,3,4) -> (2,3,4)

            # Case 3: Multiple singleton dimensions, squeezing one
            (torch.ones(1, 2, 1, 4), 2, (1, 2, 4)),  # (1,2,1,4) -> (1,2,4)

            # Case 4: Squeezing a negative index
            (torch.ones(2, 3, 1), -1, (2, 3)),  # (2,3,1) -> (2,3)

            # Case 5: Squeezing all size 1 dimensions
            (torch.ones(1, 1, 1), 0, (1, 1)),  # (1,1,1) -> (1,1)
            (torch.ones(1, 1, 1), 1, (1, 1)),  # (1,1,1) -> (1,1)
            (torch.ones(1, 1, 1), 2, (1, 1)),  # (1,1,1) -> (1,1)
        ]

    def test_squeeze(self):
        """Test tensor squeeze operation on various dimensions."""
        for input_tensor, dim, expected_shape in self.test_cases:
            with self.subTest(input_shape=input_tensor.shape, dim=dim):
                result, = self.node.f(input_tensor, dim)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result has correct shape
                self.assertEqual(result.shape, torch.Size(expected_shape), f"Expected shape {expected_shape}, got {result.shape}")

                # Ensure result has the same dtype
                self.assertEqual(result.dtype, input_tensor.dtype, "Dtype mismatch after squeeze operation")


if __name__ == "__main__":
    unittest.main()
