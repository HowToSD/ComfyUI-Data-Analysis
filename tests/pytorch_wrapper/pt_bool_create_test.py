import os
import sys
import unittest
import torch
import ast

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_bool_create import PtBoolCreate

class TestPtBoolCreate(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PtBoolCreate()

        # Test cases covering various ranks
        self.test_cases = [
            # Rank 0 (scalar)
            ("True", torch.tensor(True, dtype=torch.bool)),
            ("False", torch.tensor(False, dtype=torch.bool)),

            # Rank 1 (1D array)
            ("[True, False, True]", torch.tensor([True, False, True], dtype=torch.bool)),

            # Rank 2 (2D matrix)
            ("[[True, False], [False, True]]", torch.tensor([[True, False], [False, True]], dtype=torch.bool)),

            # Rank 3 (3D tensor)
            (
                "[[[True, False], [False, True]], [[False, True], [True, False]]]",
                torch.tensor([[[True, False], [False, True]], [[False, True], [True, False]]], dtype=torch.bool),
            ),
        ]

    def test_create_tensor(self):
        """Test PyTorch boolean tensor creation from various structured inputs."""
        for data_str, expected_tensor in self.test_cases:
            with self.subTest(data=data_str):
                retval = self.node.f(data_str)[0]

                # Ensure the returned value is a PyTorch tensor
                self.assertTrue(isinstance(retval, torch.Tensor), f"Expected tensor, got {type(retval)}")

                # Ensure the dtype is bool
                self.assertEqual(retval.dtype, torch.bool, f"Dtype mismatch for input: {data_str}")

                # Ensure the shape matches
                self.assertEqual(retval.shape, expected_tensor.shape, 
                                 f"Shape mismatch for input: {data_str} (Expected {expected_tensor.shape}, got {retval.shape})")

                # Ensure values match
                torch.testing.assert_close(retval, expected_tensor, 
                                           msg=f"Value mismatch for input: {data_str}")

if __name__ == "__main__":
    unittest.main()
