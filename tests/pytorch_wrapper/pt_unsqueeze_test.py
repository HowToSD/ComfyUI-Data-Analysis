import os
import sys
import unittest
import torch


PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_unsqueeze import PtUnsqueeze  # Importing the PtUnsqueeze class


class TestPtUnsqueeze(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtUnsqueeze()

        # Define test cases: (input_tensor, dim, expected_shape)
        self.test_cases = [
            # Case 1: Adding a singleton dimension at different positions
            (torch.ones(3, 4), 0, (1, 3, 4)),  # (3,4) -> (1,3,4)
            (torch.ones(3, 4), 1, (3, 1, 4)),  # (3,4) -> (3,1,4)
            (torch.ones(3, 4), 2, (3, 4, 1)),  # (3,4) -> (3,4,1)

            # Case 2: Adding a singleton dimension at negative indices
            (torch.ones(3, 4), -1, (3, 4, 1)),  # (3,4) -> (3,4,1)
            (torch.ones(3, 4), -2, (3, 1, 4)),  # (3,4) -> (3,1,4)
            (torch.ones(3, 4), -3, (1, 3, 4)),  # (3,4) -> (1,3,4)

            # Case 3: Adding multiple dimensions one by one
            (torch.ones(3,), 0, (1, 3)),  # (3,) -> (1,3)
            (torch.ones(3,), 1, (3, 1)),  # (3,) -> (3,1)
            (torch.ones(3,), -1, (3, 1)),  # (3,) -> (3,1)

            # Case 4: Expanding an already multi-dimensional tensor
            (torch.ones(2, 3, 4), 1, (2, 1, 3, 4)),  # (2,3,4) -> (2,1,3,4)
            (torch.ones(2, 3, 4), -1, (2, 3, 4, 1)),  # (2,3,4) -> (2,3,4,1)
        ]

    def test_unsqueeze(self):
        """Test tensor unsqueeze operation on various dimensions."""
        for input_tensor, dim, expected_shape in self.test_cases:
            with self.subTest(input_shape=input_tensor.shape, dim=dim):
                result, = self.node.f(input_tensor, dim)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result has correct shape
                self.assertEqual(result.shape, torch.Size(expected_shape), f"Expected shape {expected_shape}, got {result.shape}")

                # Ensure result has the same dtype
                self.assertEqual(result.dtype, input_tensor.dtype, "Dtype mismatch after unsqueeze operation")

if __name__ == "__main__":
    unittest.main()
