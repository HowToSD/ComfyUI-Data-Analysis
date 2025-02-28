import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_reshape import PtReshape  # Importing the PtReshape class


class TestPtReshape(unittest.TestCase):
    def setUp(self):
        """Set up test instance."""
        self.node = PtReshape()

        # Define test cases: (input_tensor, new_shape, expected_shape)
        self.test_cases = [
            # Case 1: Reshape a 2D tensor
            (torch.ones(2, 3), "[3, 2]", (3, 2)),  # (2,3) -> (3,2)

            # Case 2: Reshape a 3D tensor
            (torch.ones(2, 3, 4), "[6, 4]", (6, 4)),  # (2,3,4) -> (6,4)

            # Case 3: Using -1 for automatic inference
            (torch.ones(2, 3, 4), "[2, -1]", (2, 12)),  # (2,3,4) -> (2,12)
            (torch.ones(6, 4), "[-1, 4]", (6, 4)),  # (6,4) -> (6,4)

            # Case 4: Flattening a multi-dimensional tensor
            (torch.ones(2, 3, 4), "[-1]", (24,)),  # (2,3,4) -> (24,)

            # Case 5: Expanding dimensions
            (torch.ones(6,), "[2, 3]", (2, 3)),  # (6,) -> (2,3)

            # Case 6: Reshaping a 4D tensor
            (torch.ones(2, 3, 4, 5), "[6, -1, 5]", (6, 4, 5)),  # (2,3,4,5) -> (6,4,5)

            # Case 7: Edge case with 1D tensor
            (torch.ones(10,), "[10, 1]", (10, 1)),  # (10,) -> (10,1)
        ]

    def test_reshape(self):
        """Test tensor reshape operation with various shape orders."""
        for input_tensor, new_shape, expected_shape in self.test_cases:
            with self.subTest(input_shape=input_tensor.shape, new_shape=new_shape):
                result, = self.node.f(input_tensor, new_shape)

                # Ensure return value is a tensor
                self.assertTrue(isinstance(result, torch.Tensor), "Output is not a tensor")

                # Ensure result has correct shape
                self.assertEqual(result.shape, torch.Size(expected_shape), f"Expected shape {expected_shape}, got {result.shape}")

                # Ensure result has the same dtype
                self.assertEqual(result.dtype, input_tensor.dtype, "Dtype mismatch after reshape operation")


if __name__ == "__main__":
    unittest.main()
