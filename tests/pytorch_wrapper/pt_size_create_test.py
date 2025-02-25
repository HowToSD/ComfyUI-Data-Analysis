import os
import sys
import unittest
import torch

PROJECT_ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULE_ROOT = os.path.join(PROJECT_ROOT, "modules")
sys.path.append(MODULE_ROOT)

from pytorch_wrapper.pt_size_create import PtSizeCreate

class TestPtSizeCreate(unittest.TestCase):
    def setUp(self):
        """Set up test data."""
        self.node = PtSizeCreate()

        # Test cases with torch.Size objects
        self.test_cases = [
            # Empty size (zero-rank tensor shape)
            ("[]", torch.Size([])),
            # Rank 1 (single-dimension size)
            ("[3]", torch.Size([3])),
            # Rank 2 (matrix size)
            ("[3, 4]", torch.Size([3, 4])),
            # Rank 3 (3D tensor size)
            ("[2, 3, 4]", torch.Size([2, 3, 4])),
            # Rank 4 (higher-dimensional tensor size)
            ("[1, 2, 3, 4]", torch.Size([1, 2, 3, 4])),
            # Rank 5 (very high-dimensional tensor size)
            ("[5, 4, 3, 2, 1]", torch.Size([5, 4, 3, 2, 1])),
        ]

    def test_create_size(self):
        """Test PyTorch Size creation from various structured inputs."""
        for data_str, expected_size in self.test_cases:
            with self.subTest(data=data_str):
                retval = self.node.f(data_str)[0]

                # Ensure the returned value is a PyTorch Size
                self.assertTrue(isinstance(retval, torch.Size), f"Expected Size, got {type(retval)}")

                # Ensure the value matches expected size
                self.assertEqual(retval, expected_size, f"Value mismatch for input: {data_str}")

if __name__ == "__main__":
    unittest.main()
