import os
import sys
import unittest
import torch


PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_permute import PtPermute


class TestPtPermute(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtPermute()

        # Define test cases: (input_tensor, new_axes, expected_shape)
        self.test_cases = [
            # Case 1: Basic 2D permutation
            (torch.ones(2, 3), "[1, 0]", (3, 2)),  # (2,3) -> (3,2)

            # Case 2: Permute dimensions of a 3D tensor
            (torch.ones(2, 3, 4), "[2, 0, 1]", (4, 2, 3)),  # (2,3,4) -> (4,2,3)

            # Case 3: Identity permutation (no change)
            (torch.ones(2, 3, 4), "[0, 1, 2]", (2, 3, 4)),  # (2,3,4) -> (2,3,4)

            # Case 4: Permute 4D tensor (like a channel-first transformation)
            (torch.ones(2, 3, 96, 32), "[0, 3, 1, 2]", (2, 32, 3, 96)),  # (2,3,96,32) -> (2,32,3,96)

            # Case 5: Swapping first and last dimensions
            (torch.ones(5, 10, 15), "[2, 1, 0]", (15, 10, 5)),  # (5,10,15) -> (15,10,5)

            # Case 6: Edge case with a single-dimension tensor
            (torch.ones(10,), "[0]", (10,)),  # (10,) -> (10,) (No change)

            # Case 7: Larger 5D tensor permutation
            (torch.ones(2, 3, 4, 5, 6), "[4, 3, 2, 1, 0]", (6, 5, 4, 3, 2)),  # Reverse all dimensions
        ]

    def test_permute(self):
        """Test tensor permutation operation with various dimension orders."""
        for input_tensor, new_axes, expected_shape in self.test_cases:
            with self.subTest(input_shape=input_tensor.shape, new_axes=new_axes):
                result, = self.node.f(input_tensor, new_axes)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result has correct shape
                self.assertEqual(result.shape, torch.Size(expected_shape), f"Expected shape {expected_shape}, got {result.shape}")

                # Ensure result has the same dtype
                self.assertEqual(result.dtype, input_tensor.dtype, "Dtype mismatch after permute operation")

if __name__ == "__main__":
    unittest.main()
